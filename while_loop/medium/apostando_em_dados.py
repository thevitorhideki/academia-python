from random import randint

def apostando_em_dados(number, value, rounds):
    n = 1 
    while n <= rounds:
        dado = randint(1, 6)
        
        if dado == number:
            value += value * 1/3
        else:
            value -= value * 1/6
        n += 1
    
    return value
