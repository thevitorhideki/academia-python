def calcula_fibonacci(n):
    fibonnaci = []

    for i in range(1, n + 1):
        if i == 1:
            fibonnaci.append(1)
        elif i == 2:
            fibonnaci.append(1)
        else:
            fibonnaci.append(fibonnaci[i - 3] + fibonnaci[i - 2])

    return fibonnaci
