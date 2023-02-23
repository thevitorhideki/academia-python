def preco_passagem(km):
    if km<200:
        preco=km*0.5
        return preco
    else:
        preco=100+(0.45*(km-200))
        return preco

distancia = float(input())
print(f'{preco_passagem(distancia):.2f}')
