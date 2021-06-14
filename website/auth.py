from flask import Blueprint, render_template
# An application blueprint - defines a bunch of URLs.

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')
