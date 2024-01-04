from flask.views import MethodView
from flask import render_template, request, jsonify, session
from src.controllers.jogo_controller import forca

class carregarJogo(MethodView):
    def get (self):
        forca().sortearPalavra('Aleatorio')
        dica = session['dica']
        campo = session['campo']
        opcaoSelecionada = 'Aleatorio'
        erros = str(session['erros'])
        session['competitivo'] = False
        return render_template('index.html', campo=campo, dica=dica, opcaoSelecionada=opcaoSelecionada, erros=erros)
    
    def post (self):
        opcaoSelecionada = request.form['opcao']
        if not opcaoSelecionada: 
            opcaoSelecionada = 'Aleatorio'
        forca().sortearPalavra(opcaoSelecionada)
        dica = session['dica']
        campo = session['campo']
        erros = str(session['erros'])
        return render_template('index.html', campo=campo, dica=dica, opcaoSelecionada=opcaoSelecionada, erros=erros)
     
    
class escolher (MethodView):
    def get(self):
        escolha = request.args.get('tecla')
        if session['competitivo'] == False:
            forca().jogar(escolha)
        else:
            forca().jogarCompetitivo(escolha)
        resposta = session['campo'], session['chute'], session['partida'], session['palavra'], str(session['erros'])
        return jsonify({'message': resposta})