from database import db
from app import app
from models import User, Pet

with app.app_context():
    db.create_all()

    # Usuario de ejemplo
    user = User(name="Juan Pérez", email="juan.perez@example.com")
    db.session.add(user)

    # Mascotas de ejemplo
    pet1 = Pet(name="Firulais", type="Perro", breed="Labrador", age=3, owner=user)
    pet2 = Pet(name="Michi", type="Gato", breed="Siames", age=2, owner=user)
    db.session.add_all([pet1, pet2])

    db.session.commit()
    print("Base de datos inicializada con datos de ejemplo.")
