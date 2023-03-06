def atualiza_telefone(number: str) -> str:
    left, x, right = number.partition('-')
    if len(left) + len(right) < 9:
        return '9' + number
    elif len(number) < 8:
        return '9' + number
    return number
