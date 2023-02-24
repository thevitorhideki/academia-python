idades = []
classificacao = [[], [], [], [], [], []]
# Pergunta idades até receber um número negativo

while True:
    idade = int(input("Digite a idade: "))
    if idade < 0:
        break
    idades.append(idade)
    idades.sort()
    
# Converte a lista de idades em uma lista de valores relativos 
for i in range(len(idades)):
    if 0 <= idades[i] <= 11:
        classificacao[0].append(100/len(idades))
    elif 12 <= idades[i] <= 17:
        classificacao[1].append(100/len(idades))
    elif 18 <= idades[i] <= 25:
        classificacao[2].append(100/len(idades))
    elif 26 <= idades[i] <= 35:
        classificacao[3].append(100/len(idades))
    elif 36 <= idades[i] <= 59:
        classificacao[4].append(100/len(idades))
    else:
        classificacao[5].append(100/len(idades))

# Soma as listas de valores relativos
for i in range(len(classificacao)):
    classificacao[i] = sum(classificacao[i])

print(f"0-11 anos: {classificacao[0]:.2f} %")
print(f"12-17 anos: {classificacao[1]:.2f} %")
print(f"18-25 anos: {classificacao[2]:.2f} %")
print(f"26-35 anos: {classificacao[3]:.2f} %")
print(f"36-59 anos: {classificacao[4]:.2f} %")
print(f"Acima de 60 anos: {classificacao[5]:.2f} %")
