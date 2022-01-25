import cv2
from goprocam import GoProCamera, constants


class VideoStreaming(object):

    def __init__(self):

        self.go_pro = GoProCamera.GoPro()
        self.go_pro.livestream('start')
        self.cap = cv2.VideoCapture("udp://10.5.5.9:8554", cv2.CAP_FFMPEG)

    def set_camera(self):

        self.go_pro.video_settings(res='1080p', fps='60')
        self.go_pro.gpControlSet(constants.Stream.WINDOW_SIZE,
                                 constants.Stream.WindowSize.R720)

    def gen_frame(self):

        self.cap.set(3, 1920)
        self.cap.set(4, 1080)
        ret, frame = self.cap.read()
        ret, buffer = cv2.imencode('image.jpg', frame)
        return buffer.tobytes()

    def __del__(self):

        self.cap.release()
        cv2.destroyAllWindows()
