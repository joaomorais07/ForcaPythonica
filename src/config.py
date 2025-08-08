import os
from pathlib import Path


class Config:
    # Segurança
    SECRET_FILE_PATH = Path(".flask_secret")
    if SECRET_FILE_PATH.exists():
        with SECRET_FILE_PATH.open("r") as secret_file:
            SECRET_KEY = secret_file.read().strip()
    else:
        SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(32).hex())
        with SECRET_FILE_PATH.open("w") as secret_file:
            secret_file.write(SECRET_KEY)

    # Configuração do CORS
    CORS_HEADERS = ['Content-Type']


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
