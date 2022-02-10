from crypt import methods
from flask import Blueprint, render_template, request, Response
from flask_login import login_required
from .live import VideoStreaming, stream
from threading import Thread

main = Blueprint('main', __name__)


CAMERA_CONTROL = {

    'Take Photo': "take_photo",
    'Video': "video",  # video mode
    'Download': "download"  # downlaod media
}

CAMERA_SETTINGS = {
    '5K': '24',
    '4K': '1',
    '2K': '4',
    '1080p': '9'
}

CAMERA_FRAMES = {
    '240FPS': '0',
    '120FPS': '1',
    '60FPS': '5',
    '30FPS': '8',
    '24FPS': '10'
}

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


@main.route('/live/mode/<value>')
@login_required
def set_mode(value):
    cam = VideoStreaming()
    settings = dict(
        photo=cam.photo_mode,
        video=cam.video_mode,
        take_photo=cam.take_photo,
        start=cam.shutter_on,
        stop=cam.shutter_off
    )
    settings[value]()


@main.route('/live/resolution/<value>')
@login_required
def set_reslution(value):
    cam = VideoStreaming()
    cam.resolution(value)


@main.route('/live/fps/<value>')
@login_required
def set_fps(value):
    cam = VideoStreaming()
    cam.fps_rate(value)


@main.route('/live/fov/<value>')
@login_required
def set_fov(value):
    cam = VideoStreaming()
    cam.fov(value)


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
        elif request.form.get('record') == 'Record':
            cam.start()
            cam.record()
            thread = Thread(target=cam.record)
            thread.start()
    return render_template('videoPlayer.html')
