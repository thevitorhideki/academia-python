pergunta1=input("Tamanho [P/M/G]? ")
if pergunta1=='P':
    valor=50.0
elif pergunta1=='M':
    valor=70.0
elif pergunta1=='G':
    valor=90.0
pergunta2=input("Borda recheada [S/N]? ")
if pergunta2=='S':
    valor=valor*1.15
pergunta3=input("Adicional de queijo [S/N]? ")
if pergunta3=='S':
    if pergunta2=='S':
        valor
    valor=1.1*valor
pergunta4=input("Refrigerante [S/N]? ")
if pergunta4=='S':
    valor+=12
pergunta5=input("Sobremesa [S/N]? ")
if pergunta5=='S':
    valor+=20
    if pergunta1=='G':
        valor=valor*0.93
print(f'{valor:.2f}')
