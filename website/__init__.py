# Making the website folder a package so it can be imported
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'funkyCarrots69'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views        #importing the Blueprint
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #Checking if the database is created
    from .models import User, Note #defines the classes in .models

    create_database(app) #checking, setting up the database.

    '''
    Finding the user
    '''

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  #If the user isn't logged in
    login_manager.init_app(app)


    @login_manager.user_loader              #Decorator to load user
    def load_user(id):
        return User.query.get(int(id))

    return app

#Creating a flask application and its secret key.


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
