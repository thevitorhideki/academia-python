def soma_pecas(peaces):
    sum = 0

    for i in range(len(peaces)):
        for j in peaces[i]:
            sum += j

    return sum
