from flask import Flask
from .extentions import db

#from .instance.config import Config


def create_app():
    
    app = Flask(__name__)
    
    app.config.from_object('config.DevConfig')
    db.init_app(app)
    
    from .main.views import main

    app.register_blueprint(main)
    
    return app