from flask import Blueprint, render_template


err = Blueprint('err', __name__)


@err.app_errorhandler(404)
def error_404(error):
    return render_template('/errors/404.html'), 404


@err.app_errorhandler(403)
def error_403(error):
    return render_template('/errors/403.html'), 403


@err.app_errorhandler(500)
def error_500(error):
    return render_template('/errors/500.html'), 500
