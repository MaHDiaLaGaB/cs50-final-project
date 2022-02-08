import cv2
from time import sleep, time
import socket
from goprocam import GoProCamera, constants


class VideoStreaming(object):

    def __init__(self):

        self.go_pro = GoProCamera.GoPro()
        self.cap = None

    def start(self):

        self.go_pro.mode(mode=constants.Mode.VideoMode, submode='0')
        self.go_pro.video_settings(res='1080p', fps='60')
        self.go_pro.gpControlSet(constants.Stream.WINDOW_SIZE,
                                 constants.Stream.WindowSize.R720)
        self.go_pro.livestream('start')
        self.cap = cv2.VideoCapture("udp://10.5.5.9:8554", cv2.CAP_FFMPEG)

    def set_camera(self):
        pass

    def gen_frame(self):

        if self.cap is None:
            print('you should call start first')

        self.cap.set(3, 1920)
        self.cap.set(4, 1080)
        ret, frame = self.cap.read()
        ret, buffer = cv2.imencode('image.jpg', frame)
        print(frame.shape)
        return buffer.tobytes()

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

    def change_mode(self):
        pass

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
        frame = cam.gen_frame()
        if time() - t >= 2.5:
            live_socket.sendto(
                "_GPHD_:0:0:2:0.000000\n".encode(), ("10.5.5.9", 8554))
            t = time()
        yield (b'--frame\r\n'b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n\r\n')
