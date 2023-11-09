import random

def inicializa(palavras: list) -> dict:
    n = len(palavras[0])
    tentativas = n + 1
    especuladas = []
    sorteada = random.choice(palavras)

    return {'n': n, 'sorteada': sorteada, 'especuladas': especuladas, 'tentativas': tentativas}