from crypt import methods
from flask import Blueprint, render_template, request, Response
from flask_login import login_required
from pkg_resources import AvailableDistributions
from .live import VideoStreaming, stream


main = Blueprint('main', __name__)


START, STOP, PHOTO, VIDEO, DOWNLOAD = "start", "stop", "photo", "video", "download"
AVAILABLE_CONTROLS = {
    'Start': START,
    'Stop': STOP,
    'Photo': PHOTO,
    'Video': VIDEO,
    'Download': DOWNLOAD
}


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/live', methods=['GET'])
@login_required
def live():
    return render_template('live.html', controls=AVAILABLE_CONTROLS)


@main.route('/video_feed', methods=['GET', 'POST'])
@login_required
def video_feed():
    cam = VideoStreaming()
    cam.start()

    return Response(stream(cam), mimetype='multipart/x-mixed-replace; boundary=frame')


# @main.route('/settings', methods=['GET', 'POST'])
# @login_required
# def settings():

#     g = VideoStreaming()
#     if request.method == 'POST':
#         if request.form.get('photo') == 'Photo':
#             g.photo_mode()

#         elif request.form.get('video') == 'Video':
#             mode.mode_video()

#         elif request.form.get('super') == 'Super View':
#             mode.mode_stop()

#         elif request.form.get('stop') == 'Stop/Start':
#             mode.start_again()
#         return render_template('live.html')

#     return render_template('live.html')
