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


def primos_entre(num1, num2):
    count = 0

    for i in range(num1, num2 + 1):
        if is_prime(i) == True:
            count += 1

    return count

