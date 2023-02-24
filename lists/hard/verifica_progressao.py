def verifica_progressao(numbers: list):
    k = numbers[-1] - numbers[-2]
    q = numbers[-1] / numbers[-2]
    pa = numbers[0] + (len(numbers) - 1) * k
    pg = numbers[0] * q ** (len(numbers) - 1)

    if numbers[-1] == pa and numbers[-1] == pg:
        return 'AG'
    elif numbers[-1] == pa:
        return 'PA'
    elif numbers[-1] == pg:
        return 'PG'

    return 'NA'
