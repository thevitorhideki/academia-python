import math

def calcula_euler(x, n):
    i = 1
    soma = 1
    while i < n:
        soma += x**i / math.factorial(i)
        i += 1
         
    return soma
