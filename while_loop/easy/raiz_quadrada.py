def raiz_quadrada(num):
    count = 0
    i = 1
    while num > 0:
        num -= i
        i += 2
        count += 1
            
    return count

