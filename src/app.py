# src/app_factory.py
import os
from flask import Flask
from flask_cors import CORS
from src.config import config_dict
from src.routes.rotas import bp


def create_app():
    app = Flask(
        __name__,
        static_folder=os.path.join(os.path.dirname(__file__), 'static'),
        template_folder=os.path.join(os.path.dirname(__file__), 'templates')
    )

    # Configurações
    env = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config_dict[env])

    # CORS
    CORS(app, origins='*', headers=app.config['CORS_HEADERS'])

    # Registro de rotas
    app.register_blueprint(bp)

    return app
