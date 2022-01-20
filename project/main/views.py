from flask import Blueprint, render_template, url_for
from flask_login import login_required


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')



@main.route('/live',methods=['GET'])
@login_required
def live():
    return render_template('live.html')
