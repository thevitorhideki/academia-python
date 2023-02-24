import math

def calcula_pi(n):
    soma = 0
    
    while n > 0:
        soma += 6 / (n ** 2)
        n -= 1
        
    resultado = math.sqrt(soma)

    return resultado

