import math

carnes = {
    "patinho": ['bovina', 40],
    "acem": ['bovina', 34],
    "peito": ['frango', 24],
    "sobrecoxa": ['frango', 13],
    "bisteca": ['suina', 28]
}

total = 0
peso_bovina = 0
preco_bovina = 0
tipos = []

carne = input("Qual carne deseja? ")
while carne != 'pagar':
    if carne not in carnes:
        print("Carne nao reconhecida - tente novamente.")
    else:
        peso = float(input("Qual peso? "))
        bandeja = input("Na bandeja? (s/n): ")

        if carnes[carne][0] not in tipos:
            tipos.append(carnes[carne][0])

        if carnes[carne][0] == 'bovina':
            peso_bovina += peso

        if bandeja == 's' and peso >= 1:
            total += 0.5 * math.floor(peso)

        if carnes[carne][0] == 'bovina':
            preco_bovina += carnes[carne][1] * peso
        else:
            total += carnes[carne][1] * peso

    carne = input("Qual carne? ")

if 3 <= peso_bovina < 5:
    preco_bovina *= 0.95
elif peso_bovina >= 5:
    preco_bovina *= 0.93

total += preco_bovina

if len(tipos) == 3:
    total *= 0.9

print(f'O total da sua compra foi {total:.2f}')
