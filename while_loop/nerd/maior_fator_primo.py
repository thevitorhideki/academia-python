import math


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True


def maior_fator_primo(num):
    if is_prime(num):
        return num

    for i in range(2, int(math.sqrt(num)) + 1, 1):
        if num % i == 0 and is_prime(i):
            print(num, i)
            return maior_fator_primo(num // i)

    return num

