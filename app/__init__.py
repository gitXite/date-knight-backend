from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os


def create_app():
    load_dotenv()
    
    app = Flask(__name__)
    CORS(app, supports_credentials=True, origins=[os.getenv("FRONTEND_URL", "http://localhost:5173")])
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key')

    return app
