from flask import Blueprint
# An application blueprint - defines a bunch of URLs.

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign_up')
def sign_up():
    return "<p>sign up</p>"
