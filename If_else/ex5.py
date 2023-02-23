def testa_x_y(x, y):
    if x > y:
        resultado = 1
        return resultado
    elif x == y:
        return 0
    else:
        return -1
print(testa_x_y(10, 5))
print(testa_x_y(5, 10))
print(testa_x_y(5,5))

numero = int(input('Digite um número: '))

if numero == 42:
    print('Resposta para a vida, o universo e tudo mais')
else:
    print('Um número qualquer')