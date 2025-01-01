from flask import Flask
from database import db, db_config  

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar la base de datos
db_config(app)

# Ruta básica para verificar que la aplicación está funcionando
@app.route('/')
def index():
    return "¡PetSalud está en funcionamiento!"

if __name__ == "__main__":
    app.run(debug=True)
