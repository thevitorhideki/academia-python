import math

def encontra_uma_raiz(a, b, c):
    delta = b**2 - 4 * a * c
    
    resultado1 = (-b + math.sqrt(delta)) / (2 * a)
    resultado2 = (-b - math.sqrt(delta)) / (2 * a)
    
    return resultado1
