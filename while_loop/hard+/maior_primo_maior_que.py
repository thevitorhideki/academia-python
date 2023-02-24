def is_prime(num):
    if num == 0 or num == 1:
        return False

    divisor = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisor += 1

    if divisor > 2:
        return False

    return True


def maior_primo_menor_que(num):
    if num < 2:
        return -1

    for i in range(num, 1, -1):
        if is_prime(i):
            return i

