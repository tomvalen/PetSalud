from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Cargar las variables desde el archivo .env
load_dotenv()

db = SQLAlchemy()

def db_config(app):
    turso_database_url = os.environ.get("TURSO_DATABASE_URL")
    turso_auth_token = os.environ.get("TURSO_AUTH_TOKEN")

    print(f"TURSO_DATABASE_URL: {turso_database_url}")
    print(f"TURSO_AUTH_TOKEN: {turso_auth_token}")

    # Verificar que las variables estén configuradas
    if not turso_database_url or not turso_auth_token:
        raise ValueError("TURSO_DATABASE_URL y TURSO_AUTH_TOKEN deben estar configurados en .env")

    # Configurar la URI de la base de datos con SQLAlchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = f"{turso_database_url}/?authToken={turso_auth_token}&secure=true"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
