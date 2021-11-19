from flask import Flask, render_template, redirect, flash, session, request
from flask_debugtoolbar import DebugToolbarExtension, toolbar
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from wtforms.validators import InputRequired, Optional

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.debug = DebugToolbarExtension
app.debug = True
toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def home_page():
    """Returns home page"""
    all_pets = Pet.query.all()
    return render_template("home.html", all_pets=all_pets)

@app.route("/add", methods=['GET', 'POST'])
def Add_pet():
    """Shows WTForm for adding a pet to the db"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        photo_url = form.photo_url.data
        notes = form.notes.data
        print(name, species, age, notes, photo_url)
        new_pet = Pet(name=name, species=species, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash("Pet added succesfully!")
        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)

@app.route("/<int:id>", methods=['GET', 'POST'])
def show_edit_page(id):
    """Show edit page"""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"{pet.name} was edited correctly!")

        return redirect("/")
    else:
        return render_template("edit_pet.html", form=form, pet=pet)