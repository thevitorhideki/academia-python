from random import choice


def distribuir(n: int, numbers: list[int]) -> list[int]:
    chosen_numbers = []

    index = 1
    while index <= n:
        drawn = choice(numbers)
        if drawn not in chosen_numbers:
            chosen_numbers.append(drawn)
            index += 1

    return chosen_numbers


print(distribuir(4, [10, 1, 5, 6, 9, 15, 2]))
