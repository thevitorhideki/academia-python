def decimal_para_binario(num):
    sequence = ''

    if num < 0:
        return 'Negativo'

    while num > 0:
        sequence += str((num % 2))
        num //= 2

    binary = sequence[::-1]
    return binary

