def preco_medio(precos, dias):
    total = sum(precos)
     
    return (f"O preço médio cobrado foi de {total/dias:.2f}")

dias = int(input("Quantos dias vc quer analisar? "))
preco_dia = []

for i in range(1, dias + 1):
    preco_dia.append(float(input("Digite o preço: ")))

menor = preco_dia.index(min(preco_dia)) + 1
maior = preco_dia.index(max(preco_dia)) + 1

print(f"O dia {menor} foi o melhor dia para compra")
print(f"O dia {maior} foi o pior dia para compra")
print(preco_medio(preco_dia, dias))
