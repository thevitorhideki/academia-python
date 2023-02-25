def posicoes_possiveis(table, hand):
    possible = []

    for i in range(len(hand)):
        if len(table) == 0:
            possible.append(i)
        else:
            for j in range(len(hand[i])):
                if table[0][0] == hand[i][j]:
                    possible.append(i)
                elif table[-1][1] == hand[i][j]:
                    possible.append(i)

    return list(set(possible))


print(posicoes_possiveis([[0, 2], [2, 1], [1, 6], [6, 5], [5, 3]], [
      [1, 3], [0, 1], [4, 6], [0, 3], [0, 4], [6, 6], [0, 6]]))
