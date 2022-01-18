from flask import Flask

#from .instance.config import Config


def create_app():
    
    app = Flask(__name__)
    
    app.config.from_object('config.DevConfig')
    #app.config.from_pyfile('config.DevConfig')
   


    from .main.views import main

    app.register_blueprint(main)
    
    return app