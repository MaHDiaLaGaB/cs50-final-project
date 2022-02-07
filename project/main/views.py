from crypt import methods
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
    '5K': '24',
    '4K': '1',
    '2K': '4',
    '1080p': '9'
}

FR240, FR120, FR60, FR30, FR24 = "240fps", "120fps", "60fps", "30fps", "24fps"
CAMERA_FRAMES = {
    '240FPS': FR240,
    '120FPS': FR120,
    '60FPS': FR60,
    '30FPS': FR30,
    '24FPS': FR24
}

WIDE, MEDIUM, NARROW, SUPERVIEW, LINEAR, LINEAR_HL,  = "wide", "medium", "narrow", "superView", "linear", "linear_hl"
CAMERA_LINCE = {
    'Wide': '0',
    'Narrow': '6',
    'SuperView': '3',
    'Linear_HL': '8',  # horizon level

}


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/live', methods=['GET'])
@login_required
def live():
    return render_template('live.html', controls=CAMERA_CONTROL, camera_settings=CAMERA_SETTINGS, frams=CAMERA_FRAMES, linces=CAMERA_LINCE)


@main.route('/live/<ID>')
@login_required
def settings(ID):
    cam = VideoStreaming()
    if ID == PHOTO:
        cam.photo_mode()
    elif ID == VIDEO:
        cam.video_mode()
    elif ID == START:
        cam.shutter_on(ID)
    elif ID == STOP:
        cam.shutter_off(ID)
    elif CAMERA_SETTINGS:
        cam.resolution(ID)
    elif CAMERA_FRAMES:
        cam.fps_rate(ID)
    elif CAMERA_LINCE:
        cam.fov()
    return None


@main.route('/videoPlayer/videofeed')
@login_required
def videoFeed():
    cam = VideoStreaming()
    cam.start()
    return Response(stream(cam), mimetype='multipart/x-mixed-replace; boundary=frame')


@main.route('/videoPlayer', methods=['GET', 'POST'])
@login_required
def videoPlayer():
    cam = VideoStreaming()
    if request.method == 'POST':
        if request.form.get('start') == 'Start':
            cam.start()
        elif request.form.get('stop') == 'Stop':
            del cam
    return render_template('videoPlayer.html')
