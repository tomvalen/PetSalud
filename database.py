from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Cargar las variables desde el archivo .env
load_dotenv()

db = SQLAlchemy()

def db_config(app):
    """
    Configura la base de datos utilizando las variables de entorno.
    """
    database_url = os.getenv("TURSO_DATABASE_URL")
    auth_token = os.getenv("TURSO_AUTH_TOKEN")

    if not database_url:
        raise ValueError("TURSO_DATABASE_URL no está configurada en el archivo .env")
    if not auth_token:
        raise ValueError("TURSO_AUTH_TOKEN no está configurada en el archivo .env")

    # Configurar la URI con el token como parte del esquema
    app.config['SQLALCHEMY_DATABASE_URI'] = f"{database_url}?authToken={auth_token}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Probar conexión a la base de datos
    try:
        with app.app_context():
            db.engine.connect()
            print("Conexión a la base de datos exitosa.")
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        raise
