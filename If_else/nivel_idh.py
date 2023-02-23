def nivel_idh(idh):
    if idh < 0.350:
        return 'Sem dados'
    elif idh < 0.555:
        return 'Baixo'
    elif idh < 0.700:
        return 'Médio'
    elif idh < 0.800:
        return 'Alto'
    elif idh < 1.000:
        return 'Muito Alto'
    
print(nivel_idh(0.90))