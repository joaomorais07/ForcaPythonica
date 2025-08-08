import os
import json
import random
from flask.views import MethodView
from flask import session
from unidecode import unidecode


class Forca(MethodView):
    """Classe que implementa a lógica do jogo da Forca."""
    ERROS_MAXIMOS = 6

    @staticmethod
    def _normalizar(texto: str) -> str:
        """Remove acentos e converte o texto para maiúsculas."""
        return unidecode(texto).upper()

    @classmethod
    def _verificar_letra(cls, letra: str, palavra: str) -> bool:
        """Verifica se a letra existe na palavra (ignorando acentos e caixa)."""
        return cls._normalizar(letra) in cls._normalizar(palavra)

    @classmethod
    def _validar_letra(cls, letra: str, letra_palavra: str) -> bool:
        """Compara duas letras, ignorando acentos e caixa."""
        return cls._normalizar(letra) == cls._normalizar(letra_palavra)

    @classmethod
    def _carregar_palavras(cls) -> dict:
        """Carrega o arquivo JSON contendo as palavras organizadas por dica."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.join(base_dir, "..", "static", "json", "Palavras.json")
        caminho = os.path.normpath(caminho)

        if not os.path.exists(caminho):
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

        with open(caminho, encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def _criar_campo(palavra: str) -> str:
        """Cria o campo inicial do jogo com underscores para letras e hífens preservados."""
        return "".join("_" if letra != "-" else "-" for letra in palavra)

    # -------------------
    # Lógica do jogo
    # -------------------

    def sortear_palavra(self, opcao: str) -> dict:
        """
        Sorteia uma palavra e inicializa o estado do jogo na sessão.

        :param opcao: Categoria escolhida ou 'Aleatorio' para categoria aleatória.
        :return: Estado inicial do jogo salvo na sessão.
        """
        palavras_por_dica = self._carregar_palavras()
        dicas_disponiveis = list(map(str.strip, palavras_por_dica.keys()))

        dica_escolhida = random.choice(dicas_disponiveis) if opcao == "Aleatorio" else opcao

        print(f"Dica escolhida: {dica_escolhida}")

        palavra_sorteada = random.choice(palavras_por_dica[dica_escolhida]).upper()

        session.update({
            "dica": dica_escolhida,
            "campo": self._criar_campo(palavra_sorteada),
            "palavra": palavra_sorteada,
            "fim": False,
            "erros": 0,
            "partida": None
        })
        return session

    def _processar_jogada(self, escolha: str) -> dict:
        """
        Processa uma jogada (tentativa de letra) e atualiza o estado do jogo.

        :param escolha: Letra escolhida pelo jogador.
        :return: Estado atualizado do jogo.
        """
        campo_atual, palavra = session["campo"], session["palavra"]

        if self._verificar_letra(escolha, palavra):
            campo_atual = self._revelar_letras(campo_atual, palavra, escolha)
            session.update({"chute": "acertou", "campo": campo_atual})

            if "_" not in campo_atual:
                session.update({"fim": True, "partida": "ganhou"})
        else:
            session["erros"] += 1
            session.update({"chute": "errou", "campo": campo_atual})

            if session["erros"] >= self.ERROS_MAXIMOS:
                session.update({"fim": True, "partida": "perdeu"})

        return session

    def _revelar_letras(self, campo: str, palavra: str, escolha: str) -> str:
        """
        Revela todas as ocorrências da letra escolhida na palavra.

        :param campo: Estado atual do campo (com underscores e letras reveladas).
        :param palavra: Palavra secreta.
        :param escolha: Letra escolhida pelo jogador.
        :return: Campo atualizado com letras reveladas.
        """
        campo_lista = list(campo)
        for i, letra in enumerate(palavra):
            if self._validar_letra(escolha, letra) and letra != "-":
                campo_lista[i] = letra
        return "".join(campo_lista)

    # -------------------
    # Modos de jogo
    # -------------------
    def jogar(self, escolha: str) -> dict:
        """Executa uma jogada no modo normal."""
        return self._processar_jogada(escolha)

    def jogar_competitivo(self, escolha: str) -> dict:
        """Executa uma jogada no modo competitivo."""
        return self._processar_jogada(escolha)
