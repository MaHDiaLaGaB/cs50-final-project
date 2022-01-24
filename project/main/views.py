from flask import Blueprint, render_template, url_for, Response
from flask_login import login_required
from .live import VideoStreaming
from time import time
import socket


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/live', methods=['GET'])
@login_required
def live():
    return render_template('live.html')


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


@main.route('/video_feed')
def video_feed():
    return Response(stream(VideoStreaming()), mimetype='multipart/x-mixed-replace; boundary=frame')
