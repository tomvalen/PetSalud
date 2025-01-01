from database import db
from app import app
from models import User, Pet

with app.app_context():
    db.create_all()

    # Usuario de ejemplo
    admin = User(email="tomas.valenzu@gmail.com")
    db.session.add(admin)
    
    # Mascota de ejemplo
    pet1 = Pet(name="Firulais", type="Perro", breed="Labrador", age=3, owner=admin)
    pet2 = Pet(name="Michi", type="Gato", breed="Siames", age=2, owner=admin)
    db.session.add_all([pet1, pet2])

    db.session.commit()
    print("Base de datos inicializada con datos de ejemplo.")
