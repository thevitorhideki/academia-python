import math

def calcula_posicao(posicao_inicial, velocidade_inicial, aceleracao, tempo):
    posicao_final = posicao_inicial + velocidade_inicial * tempo + aceleracao * tempo ** 2 / 2
    
    return posicao_final 
