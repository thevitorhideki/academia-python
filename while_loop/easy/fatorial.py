def fatorial(num):
    soma = 1
    while num >= 1:
        soma *= num
        num -= 1
        
    return soma
