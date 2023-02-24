def soma_impares(numbers):
    impares = []

    for i in numbers:
        if i % 2 != 0:
            impares.append(i)

    return sum(impares)
