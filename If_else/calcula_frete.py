import math
def calcula_frete(valor_total,quantidade,fragilidade,distancia):
    if quantidade<=40:
        quantidade=1
    else:
        if quantidade%40==0:
            quantidade=int(quantidade/40)
        else:
            quantidade=int(quantidade/40)+1


    valor = 12.75 + quantidade*1.82*distancia
    if fragilidade=='S':
        valor_total=valor_total*0.0175
    else:
        valor_total=valor_total*0.008
    valor=valor+valor_total
    
    return valor

print(calcula_frete(800.99,135,'S',65.6))
''' valor total - qnt - fragil - km '''