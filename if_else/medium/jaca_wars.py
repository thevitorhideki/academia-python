import math
def cai_perto(velocidade,angulo):
    angulo=math.radians(angulo)
    d = (velocidade**2)*math.sin(2*angulo)/9.8
    if d >= 98 and d <= 102:
        return 'Acertou!'
    elif d < 98:
        return 'Muito perto'
    else:
        return 'Muito longe'




velocidade=float(input())
angulo=float(input())
print(cai_perto(velocidade,angulo))

