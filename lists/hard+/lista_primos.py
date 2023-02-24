import math


def is_prime(num):
    if num == 1 or num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True


def lista_primos(n):
    primes = []
    count = 2

    while len(primes) != n:
        if is_prime(count) == True:
            primes.append(count)
        count += 1

    return primes


print(lista_primos(6))
