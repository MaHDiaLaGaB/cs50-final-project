from flask import Blueprint, render_template, redirect, url_for,request,flash
from flask_login import login_user, logout_user, login_required
from project.extentions import db
from project.models import User
from .control import hash_password
import bcrypt


auth = Blueprint('auth', __name__ )


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        user_email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(user_email=user_email).first()
        if user:
            flash('Email address is already exists')
            return redirect(url_for('auth.login'))

        new_user = User(first_name=first_name, last_name=last_name, user_email=user_email, password=hash_password(password))
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """ check the method request if its post, 
        check if the user is already in the database,
        if its not will redirect to login page again"""
    
    if request.method == 'POST':
        user_email = request.form.get('user_email')
        password = request.form.get('password')
        #
        user = User.query.filter_by(user_email=user_email).first()

        if not user and not bcrypt.checkpw(password, user.password):
            flash('Please check your Email or Password')
            return redirect(url_for('auth.login'))

        login_user(user)
        return render_template('index.html')

    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))