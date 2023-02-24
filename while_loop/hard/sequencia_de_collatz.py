sequencias = []
for i in range(1, 999):

    count = 1
    while i != 1:
        if i % 2 == 0:
            i /= 2
            count += 1
        elif i % 2 != 0:
            i = 3 * i + 1
            count += 1
    sequencias.append(count)
maximo = sequencias.index(max(sequencias)) + 1
print(maximo)
