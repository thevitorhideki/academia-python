def calcula_preco_hamburguer(tipo_pao: str, qnt_carnes: int, salada: str, bacon: str, molho: str, queijo: str) -> float:
    total = 0

    if tipo_pao == 'australiano':
        total += 5.25
    elif tipo_pao == 'brioche':
        total += 7

    if qnt_carnes > 1:
        total += 8
        total += (qnt_carnes - 1) * 5
    elif qnt_carnes == 1:
        total += 8

    if salada == 'S':
        total += 3
    if bacon == 'S':
        total += 7.50
    if molho == 'S':
        total += 1
    if queijo == 'S':
        total += 5.40

    if total > 33:
        total *= 0.95

    return total

def calcula_valor_liquido(valor: float, origem: str) -> float:
    if origem == 'pyfood':
        return valor * 0.70
    elif origem == 'whatsapp':
        return (valor * 0.985) - 7.5

origem = input('pyfood / whatsapp')
mais_um = input('Deseja inserir mais um lanche? [S/N]')
total = 0
total_hamburgueria = 0

if mais_um == 'N':
    print('')
else:
    while mais_um == 'S':
        tipo_pao = input('Tipo do pão: ')
        qnt_carnes = int(input('Quantidade de carnes: '))
        salada = input('Salada? ')
        bacon = input('Bacon? ')
        molho = input('Molho? ')
        queijo = input('Queijo? ')
        
        preco = calcula_preco_hamburguer(tipo_pao, qnt_carnes, salada, bacon, molho, queijo)
        valor_liquido = calcula_valor_liquido(preco, origem)
        
        total += preco
        total_hamburgueria += valor_liquido

        print(f'Valor do lanche {preco:.2f}')

        mais_um = input('Deseja inserir mais um lanche? [S/N]')


    print(f'O pedido ira custar {total:.2f}')
    print(f'A hamburgueria ficara com {total_hamburgueria:.2f}')
    print('Pedido finalizado. Até mais!')
