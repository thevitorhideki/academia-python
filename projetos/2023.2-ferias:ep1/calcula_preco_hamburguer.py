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
