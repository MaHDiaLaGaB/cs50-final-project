from flask import Blueprint, render_template, redirect, url_for,request,flash
from project.extentions import db
from project.models import User
from .control import hash_password


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
            return redirect(url_for('auth.register'))

        new_user = User(first_name=first_name, last_name=last_name, user_email=user_email, password=hash_password(password))
        db.session.add(new_user)
        db.session.commit()
        print(hash_password(password))
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))