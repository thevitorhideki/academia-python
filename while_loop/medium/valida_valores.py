while True:
    valor = input("Digite um valor positivo decimal ou inteiro: ")
    if valor == '':
        print(-1)
        break
    elif float(valor) <= 0:
        print('erro de entrada')
    else:
        print(valor)
        break
