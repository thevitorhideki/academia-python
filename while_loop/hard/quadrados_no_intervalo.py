import math

def quadrados_no_intervalo(a, b):
    count = 0
    for i in range(a, b + 1):
        sqrt = round(math.sqrt(i))
        sqrt = sqrt**2
        if sqrt == i:
            count += 1
        
    return count

