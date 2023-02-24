def estritamente_crescente(numbers: list):
    if len(numbers) == 0:
        return []

    ascending = [numbers[0]]

    for i in range(len(numbers)):
        biggest = max(ascending)
        if numbers[i] > biggest:
            ascending.append(numbers[i])

    return ascending


print(estritamente_crescente([1, 3, 2, 3, 4, 6, 5]))
