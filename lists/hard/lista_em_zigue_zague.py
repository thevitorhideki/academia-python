def lista_em_zigue_zague(numbers: list[int]) -> bool:
    if len(numbers) == 0:
        return True
    elif len(numbers) == 1 and numbers[0] == 1:
        return True
    elif len(numbers) == 2 and numbers[0] == numbers[1]:
        return False

    previous = numbers[0]
    for i in range(1, len(numbers) - 1):
        if previous == numbers[i]:
            return False
        elif previous > numbers[i] and numbers[i] > numbers[i+1]:
            return False
        elif previous < numbers[i] and numbers[i] < numbers[i+1]:
            return False
        previous = numbers[i]

    return True


print(lista_em_zigue_zague([3, 11, 2, 7, 4, 9, 3]))
