from flask import Flask
from flask_login import LoginManager
from .extentions import db

#from .instance.config import Config


def create_app():
    
    app = Flask(__name__)
    
    app.config.from_object('config.DevConfig')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    # blueprint register
    from .main.views import main
    from .main.auth import auth
    app.register_blueprint(auth)
    app.register_blueprint(main)
    
    return app