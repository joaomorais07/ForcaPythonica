from flask import Flask
from flask_cors import CORS
import secrets
from pathlib import Path

app = Flask(__name__)

from src.routes.rotas import *
    
SECRET_FILE_PATH = Path(".flask_secret")

try:
    with SECRET_FILE_PATH.open("r") as secret_file:
        app.secret_key = secret_file.read()
except FileNotFoundError:
    with SECRET_FILE_PATH.open("w") as secret_file:
        app.secret_key = secrets.token_hex(32)
        secret_file.write(app.secret_key)
    
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
