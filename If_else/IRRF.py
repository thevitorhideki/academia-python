def irrf(salario,dependentes):
    if salario <= 1045:
        aliquota=7.5/100
    elif salario <= 2089.60:
        aliquota=9/100
    elif salario <= 3134.40:
        aliquota=12/100
    elif salario <= 6101.06:
        aliquota=14/100
    else:
        aliquota=671.12
    
    if salario > 6101.06:
        inss=aliquota
    else:
        inss=salario*aliquota
    base_de_calculo=salario-inss-dependentes*189.59

    if base_de_calculo <= 1903.98:
        aliquota2=0
        deducao=0
    elif base_de_calculo <= 2826.65:
        aliquota2=7.5/100
        deducao=142.80
    elif base_de_calculo <= 3751.05:
        aliquota2=15/100
        deducao=354.80
    elif base_de_calculo <= 4664.68:
        aliquota2=22.5/100
        deducao=636.13
    else:
        aliquota2=27.5/100
        deducao=869.36
    
    IRRF=base_de_calculo*aliquota2-deducao
    return IRRF

salario=float(input())
dependentes=int(input())
print(irrf(salario,dependentes))