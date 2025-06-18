import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://localhost:5173')
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
    
