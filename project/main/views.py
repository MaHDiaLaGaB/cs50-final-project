from flask import Blueprint, render_template, request, Response, send_file
from flask_login import login_required
from .live import VideoStreaming, stream

main = Blueprint('main', __name__)


CAMERA_CONTROL = {

    'Take Photo': "take_photo",
    'Shoot Video': "shoot_video",  # video mode
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
    'Linear HL': '8',  # horizon level
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
        # photo=cam.photo_mode,
        shoot_video=cam.shoot_video,
        take_photo=cam.take_photo,
        # start=cam.shutter_on,
        # stop=cam.shutter_off
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


@main.route('/videoPlayer/videofeed', methods=['GET', 'POST'])
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
        # if request.form.get('start') == 'Start':  # i just updated
        #     try:
        #         del cam
        #         cam.start()
        #     except:
        #         print('address is already in use')

        # elif request.form.get('stop') == 'Stop':
        #     try:
        #         del cam
        #     except:
        #         print('no camera to stop')
        if request.form.get('record') == 'Record':
            cam.record()

    return render_template('videoPlayer.html')


@main.route('/download',)
@login_required
def download():
    return send_file('project/videos/{}'.format(*'.mp4'), as_attachment=True)
