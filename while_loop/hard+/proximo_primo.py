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


def proximo_primo(num):
    count = 1
    while True:
        if is_prime(num + count) == True:
            return num + count
        count += 1

