from random import shuffle


def cria_pecas():
    peaces = []

    for i in range(7):
        for j in range(6, -1 + i, - 1):
            peaces.append([i, j])

    shuffle(peaces)
    return peaces


print(cria_pecas())
