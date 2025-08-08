from flask import Blueprint
from src.controllers.pagina_controller import carregarJogo, escolher

bp = Blueprint('main', __name__)

bp.add_url_rule('/', view_func=carregarJogo.as_view('jogo'))
bp.add_url_rule('/escolher', view_func=escolher.as_view('escolher'))
