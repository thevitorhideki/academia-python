from math import sqrt


def calcula_norma(array):
    for i in range(len(array)):
        array[i] **= 2

    return sqrt(sum(array))


print(calcula_norma([3, 4]))
