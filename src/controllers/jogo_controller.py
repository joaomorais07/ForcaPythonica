from flask.views import MethodView
from flask import render_template, redirect, request, url_for, jsonify, session
import random
import colorama as colorama
import json
from unidecode import unidecode
from src.app import app
import os


class forca (MethodView):
    @staticmethod
    def verificarLetraEmPalavra(escolha, palavra):
        palavra = unidecode(palavra).upper()
        if escolha in palavra:
            return True
        else:
            return False

    @staticmethod
    def validarLetra(escolha, letra):
        letra = unidecode(letra).upper()
        if escolha == letra:
            return True
        else:
            return False
    

    def sortearPalavra(self):
        file_path = os.path.join(app.static_folder, 'json', 'Palavras.json')
        with open(file_path, encoding="utf-8") as f:
            meuJson = json.load(f)
            dicas = list(map(lambda s: s.strip(), meuJson))
        
        dica = random.choice(dicas)
        palavra = random.choice(meuJson[dica])
     
        campo = palavra

        for letra in campo:
            if letra != "-":
                campo = campo.replace(letra, "_")
                
        session['dica'] = dica  
        session['campo'] = campo
        session['palavra'] = palavra
        session['fim'] = False
        session['erros'] = 0
        session['partida'] = None
        
        return session
        
        
    def jogar (self, escolha):
        campo = session['campo']
        palavra = session['palavra']

        if forca().verificarLetraEmPalavra(escolha, palavra):
            posicoes = []
            letras = []
            cont = 0
            for letra in palavra:
                if forca().validarLetra(escolha, letra) and letra != "-":
                    posicoes.append(cont)
                    letras.append(letra)
                cont += 1

            campo = list(campo)
            cont = 0
            for posicao in posicoes:
                campo[posicao] = letras[cont]
                cont += 1
            campo = "".join(campo)

            session['chute'] = 'acertou'      
            session['campo'] = campo
            
            if not "_" in campo:
                session['fim'] = True
                session['partida'] = 'ganhou'
                
            else:
                return session
                
        else:
            session['erros'] += 1
            session['chute'] = 'errou'
            session['campo'] = campo
            
            if session['erros'] > 6:
                session['fim'] = True
                
                session['partida'] = 'perdeu'
                return session    
                    
            else:
                return session
            
            

                