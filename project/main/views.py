from flask import Blueprint, render_template, Response


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/register', methods=['GET'])
def signup():
    return render_template('register.html')


@main.route('/login',methods=['GET'])
def login():
    return render_template('login.html')
