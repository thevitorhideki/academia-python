soma = 0

while True:
    num = input("Escreva um número: ")
    if num == '':
        break
    soma += float(num)
    if num == '0':
        print(soma)
        break
