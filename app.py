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

# Ruta para el chatbot
@app.route('/chat', methods=['POST'])
def chatbot():
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

@app.route('/chat-ui')
def chat_ui():
    return render_template('chat.html')