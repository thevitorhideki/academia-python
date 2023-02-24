def verifica_lista(numbers):
    if len(numbers) == 0:
        return 'misturado'

    for i in range(len(numbers)):
        numbers[i] %= 2

    if 1 in numbers and 0 in numbers:
        return 'misturado'
    elif sum(numbers) == 0:
        return 'par'

    return 'ímpar'
