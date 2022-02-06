import cv2
from time import sleep, time
import socket
from goprocam import GoProCamera, constants


class VideoStreaming(object):

    def __init__(self):

        self.go_pro = GoProCamera.GoPro()
        self.cap = None

    def start(self):

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
        return buffer.tobytes()

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

    def res_5k(self):
        self.go_pro.gpControlSet(
            param=constants.Video.RESOLUTION, value=constants.Video.Resolution.R5K)

    def res_4k(self):
        self.go_pro.gpControlSet(
            param=constants.Video.RESOLUTION, value='1')

    def res_2k(self):
        self.go_pro.gpControlSet(
            param=constants.Video.RESOLUTION, value=constants.Video.Resolution.R2k)

    def res_1080p(self):
        self.go_pro.gpControlSet(
            param=constants.Video.RESOLUTION, value='9')

    def fps_240(self):
        self.go_pro.gpControlSet(
            param=constants.Video.FRAME_RATE, value=constants.Video.FrameRate.FR240)

    def fps_120(self):
        self.go_pro.gpControlSet(
            param=constants.Video.FRAME_RATE, value=constants.Video.FrameRate.FR120)

    def fps_60(self):
        self.go_pro.gpControlSet(
            param=constants.Video.FRAME_RATE, value=constants.Video.FrameRate.FR60)

    def fps_30(self):
        self.go_pro.gpControlSet(
            param=constants.Video.FRAME_RATE, value=constants.Video.FrameRate.FR30)

    def fps_24(self):
        self.go_pro.gpControlSet(
            param=constants.Video.FRAME_RATE, value=constants.Video.FrameRate.FR24)

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
