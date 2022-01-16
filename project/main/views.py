import cv2
from flask import Blueprint, render_template


main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@main.route('/login',methods=['GET'])
def login():
    return render_template('login.html')
