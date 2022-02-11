import cv2
import os
from time import sleep, time
import socket
from goprocam import GoProCamera, constants

FRAME_DIMENSION = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}


class VideoStreaming(object):

    def __init__(self):

        self.go_pro = GoProCamera.GoPro()
        self.cap = None

    def start(self):

        self.go_pro.mode(mode=constants.Mode.VideoMode, submode='0')
        self.go_pro.gpControlSet(param='2', value='9')
        self.go_pro.gpControlSet(param='3', value='5')
        self.go_pro.gpControlSet(constants.Stream.WINDOW_SIZE,
                                 constants.Stream.WindowSize.R720)
        self.go_pro.livestream('start')
        self.cap = cv2.VideoCapture("udp://10.5.5.9:8554", cv2.CAP_FFMPEG)

    # recording functions --------->
    def record_resolution(self, width, height):
        if self.cap is None:
            return
        self.cap.set(3, width)
        self.cap.set(4, height)

    def get_dimension(self, res):
        # if res in the argument was empty or not accutare line 46 will work
        width, height = FRAME_DIMENSION["480p"]
        if res in FRAME_DIMENSION:
            width, height = FRAME_DIMENSION[res]
        # change the current caputre device
        # to the resulting resolution
        self.record_resolution(width, height)
        return width, height

    def get_video_type(self):
        ext = os.path.splitext('test-video.avi')
        if ext in VIDEO_TYPE:
            return VIDEO_TYPE[ext]
        return VIDEO_TYPE['avi']

    def start_record(self):
        out = cv2.VideoWriter('test-video.avi', self.get_video_type(
        ), 25, self.get_dimension('1080p'))
        return out

    # recording functions end here ------>

    def gen_frame(self):

        if self.cap is None:
            print('you should call start first')

        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        ret, frame = self.cap.read()
        if not ret:
            print('there is an error')
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, buffer = cv2.imencode('image.jpg', frame)
        # print(frame.shape)
        return (buffer.tobytes(), frame)

    # --- recording function ----

    def record(self, out):
        while True:
            out.write(self.gen_frame()[1])

    # --- controling camera functions ----

    def take_photo(self):
        self.go_pro.take_photo(2)
        sleep(0.5)

    def shutter_on(self):
        self.go_pro.shutter('1')
        sleep(0.5)

    def shutter_off(self):
        self.go_pro.shutter('0')
        sleep(0.5)

    def photo_mode(self):
        self.go_pro.mode(mode=constants.Mode.PhotoMode, submode='0')
        sleep(0.5)

    def video_mode(self):
        self.go_pro.mode(mode=constants.Mode.VideoMode, submode='0')
        sleep(0.5)

    def resolution(self, res):
        self.go_pro.gpControlSet(param='2', value=res)

    def fps_rate(self, fps):
        self.go_pro.gpControlSet(param='3', value=fps)

    def fov(self, lince):
        self.go_pro.gpControlSet(param='121', value=lince)

    def __del__(self):
        if self.cap is None:
            print('no camera to stop')

        try:
            self.go_pro.livestream('stop')
            self.cap.release()
        except:
            print('no stream to release')
        # cv2.destroyAllWindows()


def stream(cam):
    live_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    t = time()
    while True:
        frame = cam.gen_frame()[0]
        if time() - t >= 2.5:
            live_socket.sendto(
                "_GPHD_:0:0:2:0.000000\n".encode(), ("10.5.5.9", 8554))
            t = time()
        yield (b'--frame\r\n'b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n\r\n')
