def calcula_segredo(x):
    if x>999 or x<100:
        return -1
    else:
        centenas = x // 100
        dezenas = (x % 100) // 10
        unidades = x % 10
        return centenas + dezenas + unidades
    
print(calcula_segredo(123))