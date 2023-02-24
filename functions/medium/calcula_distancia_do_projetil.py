import math

def calcula_distancia_do_projetil(velocidade, angulo, altura_inicial):
    gravidade = 9.8
    
    distancia = (velocidade ** 2 / (2 * gravidade)) * (1 + math.sqrt(1 + (2 * gravidade * altura_inicial) / (velocidade ** 2 * (math.sin(angulo)) ** 2))) * math.sin(2 * angulo)
    
    return distancia
