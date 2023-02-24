# Linha
# [0][0] [0][1] [0][2]
# [1][0] [1][1] [1][2]
# [2][0] [2][1] [2][2]

# Coluna
# [0][0] [1][0] [2][0]
# [0][1] [1][1] [2][1]
# [0][2] [1][2] [2][2]

# Diagonal
# [0][0] [1][1] [2][2]
# [0][2] [1][1] [2][0]

def verifica_jogo_da_velha(game: list):
    line = 0
    column = 0

    while line <= 2:
        if game[line].count('X') == 3:
            return 'X'
        elif game[line].count('O') == 3:
            return 'O'
        line += 1


print(verifica_jogo_da_velha(
    [['X', 'O', 'O'], ['.', 'O', 'X'], ['X', 'X', 'X']]))
