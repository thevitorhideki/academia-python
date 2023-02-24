from math import sqrt


def calcula_extensao(axis_x, axis_y):
    distance = 0

    for i in range(0, len(axis_x) - 1):
        distance += sqrt((axis_x[i + 1] - axis_x[i]) ** 2 +
                         (axis_y[i + 1] - axis_y[i]) ** 2)

    return distance
