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


def primos_entre(a, b):
    primes = []

    for i in range(a, b + 1):
        if is_prime(i) == True:
            primes.append(i)

    return primes
