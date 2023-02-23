velocidade=float(input())
if velocidade>80:
    velocidade=(velocidade-80)*5
    print(f'R${velocidade:.2f}')
else:
    print('Não foi multado')