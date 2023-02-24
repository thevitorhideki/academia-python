def soma_multiplos(num1, num2):
    multiplo = 0
    soma = 0
    
    while multiplo <= num1 * 10 or multiplo <= num2 * 10:
        if multiplo % num1 == 0 or multiplo % num2 == 0:
            soma += multiplo
        multiplo += 1
    
    return soma
