from random import choice

def sorteia_questao(questoes: dict, nivel: str) -> dict:
   return choice(questoes[nivel]) 
