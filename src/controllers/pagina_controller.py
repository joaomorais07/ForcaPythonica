from flask.views import MethodView
from flask import render_template, redirect, request, jsonify, session
from src.controllers.jogo_controller import forca

class carregarIndex(MethodView):
    def get (self):
        forca().sortearPalavra()
        dica = session['dica'].upper()
        campo = session['campo']
        return render_template('index.html', campo=campo, dica=dica)
     
    
class escolher (MethodView):
    def get(self):
        escolha = request.args.get('tecla')
        forca().jogar(escolha)
        print(session['erros'])
        campo = session['campo'], session['chute'], session['partida'], session['erros'], session['palavra']

        return jsonify({'message': campo})