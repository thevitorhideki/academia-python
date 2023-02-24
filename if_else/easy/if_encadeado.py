def testa_maioridade(idade):
    if idade >= 21:
        return 'Maior nos EUA e BRASIL'
    else:
        if idade >= 18:
            return 'Maior no BRASIL'
        else:
            return 'Menor de idade'

print(testa_maioridade(17))
print(testa_maioridade(20))
print(testa_maioridade(21))

esta_quente = False

if esta_quente:
    print('Vou tomar sopa')
else:
    print('Não vou tomar sopa')