import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy.sql.visitors import ReplacingCloningVisitor

db = SQLAlchemy()

DEFAULT_IMG = "https://www.freeiconspng.com/uploads/animal-pet-dog-icon-13.png"

def connect_db(app):
    """From within app.py we import this function to connect our Flask app to our db"""
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    species = db.Column(db.String(40), nullable=False)
    photo_url = db.Column(db.String(300), default = DEFAULT_IMG)
    age = db.Column(db.Integer)
    notes = db.Column(db.String(600))
    available = db.Column(db.Boolean, default = True)

