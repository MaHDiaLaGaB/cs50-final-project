from flask import Blueprint, render_template, url_for, Response
from flask_login import login_required
from .live import LiveStreaming


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/live', methods=['GET'])
@login_required
def live():
    return render_template('live.html')


# def stream(camera):
#     while True:
#         frame = camera.gen_frames()
#         yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# @main.route('/video_feed')
# def video_feed():
#     return Response(stream(LiveStreaming()), mimetype='multipart/x-mixed-replace; boundary=frame')
