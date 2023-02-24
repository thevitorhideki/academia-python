def encontra_maximo(matriz):
    biggest = 0

    for i in range(len(matriz)):
        for j in matriz[i]:
            j = abs(j)
            if j > biggest:
                biggest = j

    return biggest


print(encontra_maximo([[1, 2, 3], [-10, 5, 6], [7, 8, 9]]))
