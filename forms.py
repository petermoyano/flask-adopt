from typing import Optional
from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import BooleanField
from wtforms.validators import Optional


class AddPetForm(FlaskForm):
    name = StringField("name")
    species = SelectField('species', choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Horse', 'Horse'), ('Rabbit', 'Rabbit')])
    photo_url = StringField("photo_url", validators=[Optional()])
    ages = [(num, num) for num in range(31)]
    age = SelectField("age", choices = ages)
    notes = StringField("notes")
    

class EditPetForm(FlaskForm):
    photo_url = StringField("photo_url", validators=[Optional()])
    notes = StringField("notes")
    TrueOrFalse = [(w, w)for w in [True, False]]
    available = BooleanField("available")