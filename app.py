from flask import Flask, request, jsonify, render_template
from openai import ChatCompletion, OpenAI
from dotenv import load_dotenv
from database import db, db_config
from models import User, Pet
import os

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__, template_folder="templates")
db_config(app)

# Cargar la clave de OpenAI desde el archivo .env
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY no está configurado en el archivo .env")

# Configurar la API de OpenAI
ChatCompletion.api_key = openai_api_key

# Rutas principales
@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/user')
def user_dashboard():
    """
    Página de ejemplo para mostrar datos del usuario.
    """
    return render_template('user.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    """
    Maneja la interfaz de usuario del chat y las solicitudes del chatbot.
    """
    if request.method == 'GET':
        # Renderizar la interfaz de usuario del chat
        return render_template('chat.html')

    if request.method == 'POST':
        # Procesar la solicitud del chatbot
        print(f"Headers recibidos: {request.headers}")
        print(f"Datos recibidos: {request.json}")
        data = request.json
        user_message = data.get('message', '')

        try:
            response = ChatCompletion.create(
                model="gpt-3.5",
                messages=[
                    {"role": "system", "content": "Eres un agente de atención al cliente para una veterinaria que ofrece los servicios de Destartraje Canino, Destartraje Felino, Esterilización Canina, Esterilización Felina, Peluquería Canina y Peluquería Felina. Sé profesional, servicial y amable."},
                    {"role": "user", "content": user_message}
                ]
            )

            bot_reply = response['choices'][0]['message']['content']
            return jsonify({"reply": bot_reply})

        except Exception as e:
            return jsonify({"error": str(e)}), 500


# Inicializar la base de datos y sus modelos
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
