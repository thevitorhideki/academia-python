def zera_negativos(array):
    for i in range(len(array)):
        if array[i] < 0:
            array[i] = 0

    return array
