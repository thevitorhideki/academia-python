# Vencer em linha
# [0][0] [0][1] [0][2]
# [1][0] [1][1] [1][2]
# [2][0] [2][1] [2][2]

# Vencer em coluna
# [0][0] [1][0] [2][0]
# [0][1] [1][1] [2][1]
# [0][2] [1][2] [2][2]

# Vencer em diagonal
# [0][0] [1][1] [2][2]
# [0][2] [1][1] [2][0]

def verifica_jogo_da_velha(game: list[list[str]]):
    # Vencer em linha
    for i in game:
        if i.count('X') == 3:
            return 'X'
        elif i.count('O') == 3:
            return 'O'

    # Vencer em coluna
    for i in range(len(game)):
        if game[0][i] == 'X' and game[1][i] == 'X' and game[2][i] == 'X':
            return 'X'
        elif game[0][i] == 'O' and game[1][i] == 'O' and game[2][i] == 'O':
            return 'O'

    # Vencer em diagonal
    if game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
        return 'X'
    elif game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
        return 'O'
    elif game[0][2] == 'X' and game[1][1] == 'X' and game[2][0] == 'X':
        return 'X'
    elif game[0][2] == 'O' and game[1][1] == 'O' and game[2][0] == 'O':
        return 'O'

    return 'V'
