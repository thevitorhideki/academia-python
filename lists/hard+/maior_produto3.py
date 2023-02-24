def maior_produto3(numbers: list[int]):
    prod = []

    for i in numbers:
        abs(i)
        numbers.sort()

    prod.append(numbers[-1] * numbers[-2] * numbers[-3])
    prod.append(numbers[0] * numbers[1] * numbers[-1])

    return max(prod)


print(maior_produto3([-10, -20, 20, 1]))
