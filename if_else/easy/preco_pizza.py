pergunta1=input("Tamanho [P/M/G]? ")
if pergunta1=='P':
    valor=50.0
elif pergunta1=='M':
    valor=70.0
elif pergunta1=='G':
    valor=90.0

pergunta2=input("Borda recheada [S/N]? ")

pergunta3=input("Adicional de queijo [S/N]? ")

pergunta4=input("Refrigerante [S/N]? ")

pergunta5=input("Sobremesa [S/N]? ")

if pergunta2 == 'S' and pergunta3=='S':
    valor=valor*1.25
elif pergunta2 == 'S' and pergunta3!='S':
    valor=valor*1.15
elif pergunta2!='S' and pergunta3=='S':
    valor=valor*1.10

if pergunta4=='S':
    valor+=12

if pergunta5=='S':
    if pergunta1=='G':
        valor+=20
        valor=0.93*valor
    else:
        valor+=20
        


print(f'{valor:.2f}')
