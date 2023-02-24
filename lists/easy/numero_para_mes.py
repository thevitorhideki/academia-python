mes = int(input("Digite o número do mês: "))

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

for i in range(len(meses)):
    if mes == i + 1:
        print(meses[i])
