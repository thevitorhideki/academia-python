def classifica_lista(numbers: list):
    if len(numbers) < 2:
        return 'nenhum'

    for i in range(len(numbers)):
        if numbers[i-1] == numbers[i]:
            return 'nenhum'

    if numbers == sorted(numbers):
        return 'crescente'
    elif numbers == sorted(numbers, reverse=True):
        return 'decrescente'

    return 'nenhum'
