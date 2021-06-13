# Making the website folder a package so it can be imported
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'funkyCarrots69'

    from .views import views        #importing the Blueprint
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app

#Creating a flask application and its secret key.
