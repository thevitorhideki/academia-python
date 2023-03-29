def gera_direcoes(x, y):
    moves = []

    for i in range(len(x) - 1):
        if y[i] == y[i+1]:
            if x[i] < x[i + 1]:
                moves.append('leste')
            elif x[i] > x[i + 1]:
                moves.append('oeste')
        elif x[i] == x[i+1]:
            if y[i] < y[i+1]:
                moves.append('sul')
            if y[i] > y[i+1]:
                moves.append('norte')
        elif x[i] < x[i+1]:
            if y[i] < y[i+1]:
                moves.append('sudeste')
            elif y[i] > y[i+1]:
                moves.append('nordeste')
        elif x[i] > x[i+1]:
            if y[i] < y[i+1]:
                moves.append('sudoeste')
            elif y[i] > y[i+1]:
                moves.append('noroeste')

    return moves
