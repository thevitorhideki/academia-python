from math import sqrt


def calcula_extensao(axis_x: list[int], axis_y: list[int]) -> float:
    distance = 0

    for i in range(0, len(axis_x) - 1):
        distance += sqrt((axis_x[i + 1] - axis_x[i]) ** 2 +
                         (axis_y[i + 1] - axis_y[i]) ** 2)

    return distance


def caminho_mais_curto(paths: list[list[list[int]]]) -> list[list[int]]:
    distance = []

    for path in paths:
        axis_x = [x[0] for x in path]
        axis_y = [y[1] for y in path]
        distance.append(calcula_extensao(axis_x, axis_y))

    return paths[distance.index(min(distance))]


print(caminho_mais_curto([
    [[5, 2], [3, 7], [7, 3], [10, 4]],
    [[5, 2], [300, 1000], [10, 4]],
]))
