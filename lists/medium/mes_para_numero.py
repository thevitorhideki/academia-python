mes = input("Digite o mês: ")

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

for i in range(len(meses)):
    if meses[i] == mes:
        print(i + 1)
