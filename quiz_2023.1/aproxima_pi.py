from math import sqrt

def aproxima (n):
    serie = 0
    i = 1
    impares = 1
    tres = 1
    while i <= n:
        if i % 2 != 0:
            serie += 1/(impares*tres) 
        else:
            serie -= 1/(impares*tres)
        tres = 3**i
        impares += 2
        i += 1
    pi = sqrt(12)*serie
    return pi