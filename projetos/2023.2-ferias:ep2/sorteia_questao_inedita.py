from random import choice

def sorteia_questao(questoes: dict, nivel: str) -> dict:
   return choice(questoes[nivel]) 

def sorteia_questao_inedita(questoes: dict, nivel: str, questoes_sorteadas: list) -> dict:
    questao_sorteada = sorteia_questao(questoes, nivel)

    while questao_sorteada in questoes_sorteadas:
        questao_sorteada = sorteia_questao(questoes, nivel)

    questoes_sorteadas.append(questao_sorteada)

    return questao_sorteada
