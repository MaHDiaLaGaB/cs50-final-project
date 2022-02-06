from flask import Blueprint, render_template, request, Response
from flask_login import login_required
from .live import VideoStreaming, stream
from time import sleep, time

main = Blueprint('main', __name__)


START, STOP, PHOTO, VIDEO, DOWNLOAD = "start", "stop", "photo", "video", "download"
CAMERA_CONTROL = {
    'Start': START,  # shutter on
    'Stop': STOP,  # shutter off
    'Photo': PHOTO,  # photo mode
    'Video': VIDEO,  # video mode
    'Download': DOWNLOAD  # downlaod media
}
FIVE_K, FOUR_K, TWO_K, FULL_HD = "5k", "4k", "2k", "1080p"
CAMERA_SETTINGS = {
    '5K': FIVE_K,
    '4K': FOUR_K,
    '2K': TWO_K,
    '1080p': FULL_HD
}

FR240, FR120, FR60, FR30, FR24 = "240fps", "120fps", "60fps", "30fps", "24fps"
CAMERA_FRAMES = {
    '240FPS': FR240,
    '120FPS': FR120,
    '60FPS': FR60,
    '30FPS': FR30,
    '24FPS': FR24
}


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/live', methods=['GET'])
@login_required
def live():
    return render_template('live.html', controls=CAMERA_CONTROL, camera_settings=CAMERA_SETTINGS, frams=CAMERA_FRAMES)


@main.route('/live/<ID>')
@login_required
def settings(ID):
    cam = VideoStreaming()
    if ID == START:
        return cam.shutter_on()
    elif ID == STOP:
        return cam.shutter_off()
    elif ID == PHOTO:
        return cam.photo_mode()
    elif ID == VIDEO:
        return cam.video_mode()
    elif ID == FIVE_K:
        return cam.res_5k()
    elif ID == FOUR_K:
        return cam.res_4k()
    elif ID == TWO_K:
        return cam.res_2k()
    elif ID == FULL_HD:
        return cam.res_1080p()
    elif ID == FR240:
        return cam.fps_240()
    elif ID == FR120:
        return cam.fps_120()
    elif ID == FR60:
        return cam.fps_60()
    elif ID == FR30:
        return cam.fps_30()
    elif ID == FR24:
        return cam.fps_24()
    return 'tnx'


@main.route('/stream')
@login_required
def stream():
    return render_template('stream.html')


@main.route('/stream/videofeed')
@login_required
def videoFeed():
    cam = VideoStreaming()
    cam.start()
    return Response(stream(cam), mimetype='multipart/x-mixed-replace; boundary=frame')

# @main.route('/stream/videofeed', methods=['GET', 'POST'])
# @login_required
# def videoFeed():
#     if request.method == 'POST':
#         if request.form.get('start') == 'Start':
#             cam = VideoStreaming()
#             cam.start()
#             return Response(stream(cam), mimetype='multipart/x-mixed-replace; boundary=frame')
#         if request.form.get('stop') == 'Stop':
#             pass
#     return 'nothing'


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
