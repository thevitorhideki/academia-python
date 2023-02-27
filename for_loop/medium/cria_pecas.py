from random import shuffle


def cria_pecas():
    pieces = []

    for i in range(7):
        for j in range(i, 7):
            pieces.append([i, j])

    shuffle(pieces)

    return pieces
