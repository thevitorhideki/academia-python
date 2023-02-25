def inicia_jogo(players: int, peaces: list):
    result = {
        'jogadores': {},
        'monte': [],
        'mesa': []
    }
    j = 0
    for i in range(players):
        result['jogadores'][i] = peaces[j:j+7]
        peaces[j:]
        j += 7

    result['monte'] = peaces[j:]

    return result


print(inicia_jogo(4, [
    [1, 3], [0, 1], [4, 6], [0, 3], [0, 4], [6, 6], [0, 6],
    [1, 1], [1, 2], [0, 0], [1, 4], [1, 5], [1, 6], [2, 2],
    [3, 6], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [2, 3],
    [3, 5], [4, 4], [4, 5], [0, 2], [5, 5], [5, 6], [0, 5]
]))
