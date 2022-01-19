
from flask import Blueprint, render_template, redirect, url_for,request

auth = Blueprint('auth', __name__ )



@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))