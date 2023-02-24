dias = int(input("Digite a quantidade de dias que deseja analisar: "))
preco = 0

for i in range(dias):
    preco += float((input("Digite o preço: ")))
    
print(f"O preço médio cobrado foi de {preco/dias:.2f}")
