# where the users can navigate to but itsn't authentication

from flask import Blueprint, render_template
# An application blueprint - defines a bunch of URLs.

views = Blueprint('views', __name__)

@views.route('/')
def home():                 #root
    return render_template("home.html")
