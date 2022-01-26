from crypt import methods
from flask import Blueprint, render_template, url_for, Response
from flask_login import login_required
from .live import VideoStreaming, stream


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/live', methods=['GET'])
@login_required
def live():
    return render_template('live.html')


@main.route('/video_feed')
def video_feed():
    return Response(stream(VideoStreaming()), mimetype='multipart/x-mixed-replace; boundary=frame')
