from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .config import DevelopmentConfig, ProductionConfig, TestingConfig
import os


def create_app(config_name='development'):
    load_dotenv()
    app = Flask(__name__)
    CORS(app, supports_credentials=True, origins=[os.getenv("FRONTEND_URL", "http://localhost:5173")])

    if config_name == "production":
        app.config.from_object(ProductionConfig)
    elif config_name == "testing":
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)   

    return app
