import math


def is_prime(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def verifica_primos(numbers: list) -> dict:
    primes = {k: True for k in numbers}

    for i in numbers:
        if is_prime(i) == True:
            primes[i] = True
        else:
            primes[i] = False

    return primes
