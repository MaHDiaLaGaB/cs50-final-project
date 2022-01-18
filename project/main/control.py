import requests
from goprocam import GoProCamera, constants

gp = GoProCamera.GoPro()
def stream():
    stream = gp.gpControlCommand(param='')
    return stream

