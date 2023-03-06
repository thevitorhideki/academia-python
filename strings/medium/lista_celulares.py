def lista_celulares(numbers: list) -> list:
    valid_numbers = []
    for i in numbers:
        if i[0] == '+' and len(i) == 14:
            valid_numbers.append(i[5:])
        elif len(i) == 11:
            valid_numbers.append(i[2:])
        elif len(i) == 9:
            valid_numbers.append(i)

    return valid_numbers
