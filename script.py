from sqlalchemy import create_engine

# URI de la base de datos y token
TURSO_DATABASE_URL = "sqlite+libsql://petsalud-tomvalen.turso.io:443"
TURSO_AUTH_TOKEN = "nuevo_token_generado"

try:
    # Crear el motor de conexión
    print("Intentando conectar a la base de datos...")
    engine = create_engine(f"{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true")
    connection = engine.connect()
    
    # Si la conexión es exitosa
    print("¡Conexión exitosa a la base de datos!")
    connection.close()
    engine.dispose()

except Exception as e:
    # Si ocurre un error, imprimirlo
    print("Error al conectar con la base de datos:", e)
