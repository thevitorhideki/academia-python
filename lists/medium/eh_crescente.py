def eh_crescente(numbers: list):
    new_numbers = sorted(numbers)

    if len(numbers) == 1:
        return True

    for i in range(len(numbers)):
        if numbers[i-1] == numbers[i]:
            return False

    if new_numbers == numbers:
        return True

    return False


print(eh_crescente([1, 2]))
