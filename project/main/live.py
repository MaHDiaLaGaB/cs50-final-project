# import cv2
# import requests
# from goprocam import GoProCamera, constants

# requests.get('http://10.5.5.9/gp/gpControl/execute?p1=gpStream&c1=start')


# class LiveStreaming(object):
#     def __init__(self):

#         self.camera = cv2.VideoCapture()

#     def __del__(self):
#         self.camera.release()

#     def gen_frames(self):

#         ret, frame = self.camera.read()
#         ret, buffer = cv2.imencode('jpg', frame)
#         frame = buffer.tobytes()
#         return frame
