from flask import Flask
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from src.routes.rotas import *

if __name__ == '__main__':
    app.run(debug=True)

app.config['SECRET_KEY'] = "senha"