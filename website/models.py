#Database structure for user, structure for notes

from . import db #importing from the same package
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  #Unique key for each ID
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    notes = db.relationship('Note')               #Relationship between the notes and user.


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(5000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())  #adding current dateTime of the object.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))         #Foreign key - associating different info with different users. References another database coloumn
    #One to many databse relation. The foreign key is for the child which references the parent.
