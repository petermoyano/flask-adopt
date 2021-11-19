from models import Pet
from app import app, db

db.drop_all()
db.create_all()

def Add_seed_pets():
    """Fills db with 3 pets ment for testing"""
    pet1 = Pet(name = "Rogger", species = "Rabbit",  photo_url = "https://www.freeiconspng.com/uploads/brown-rabbit-png-0.png",
    age = 2, notes = "Has a cute girlfriend", available = True)

    pet2 = Pet(name = "Winco", species = "Dog",  photo_url = "https://www.freeiconspng.com/uploads/dog-png-33.png",
    age = 5, notes = "Bites other dogs! Not people though", available = False)

    pet3 = Pet(name = "Flecha", species = "Horse",  photo_url = "https://www.freeiconspng.com/uploads/white-horse-3d-animal-png-7.png",
    age = 6, notes = "Donkey ears!", available = True)

    db.session.add(pet1)
    db.session.add(pet2)
    db.session.add(pet3)
    db.session.commit()

Add_seed_pets()