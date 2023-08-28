from flask import Flask
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

from src.routes.rotas import *

if __name__ == '__main__':
    app.run(debug=True)
    
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = "senha"