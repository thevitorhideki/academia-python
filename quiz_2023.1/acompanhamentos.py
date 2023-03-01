tamanho = input("Qual o tamanho do bolo? ")
orcamento = float(input("Qual o orçamento disponível? "))

tamanhos = {'XP': 5, 'P': 7, 'M': 20, 'G': 31, 'XG': 50}
acompanhamentos_count = [0, 0]
count = 0

while orcamento - tamanhos[tamanho] >= 0:
    orcamento -= tamanhos[tamanho]
    count += 1

if orcamento == 0:
    print('sem acompanhamento')

while orcamento > 0:
    if orcamento % 2 == 0:
        acompanhamentos_count[0] += 1
        orcamento -= 2
    else:
        acompanhamentos_count[1] += 1
        orcamento -= 1

if count <= 4:
    if acompanhamentos_count[0] != 0:
        print(f'{acompanhamentos_count[0]} cheesecake')
    if acompanhamentos_count[1] != 0:
        print(f'{acompanhamentos_count[1]} brownie')
else:
    if acompanhamentos_count[0] != 0:
        print(f'{acompanhamentos_count[0]} cupcake')
    if acompanhamentos_count[1] != 0:
        print(f'{acompanhamentos_count[1]} banoffee')
