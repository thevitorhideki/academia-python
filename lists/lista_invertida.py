list = []

while True:
    num = int(input("Digite um número inteiro positivo: "))

    if num > 0:
        list.append(num)
    else:
        break

print(list[::-1])
