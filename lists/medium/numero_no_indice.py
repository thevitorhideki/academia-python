def numero_no_indice(numbers):
    result = []

    for i in numbers:
        if i == numbers.index(i):
            result.append(i)

    return result
