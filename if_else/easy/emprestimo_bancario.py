valor_casa=float(input())
salario=float(input())
anos=int(input())


valor_prestacao=valor_casa/(anos*12)

if valor_prestacao > 0.3*salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
