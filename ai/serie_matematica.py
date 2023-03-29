import math


def serie(n):
    sum = 0
    i = 0
    j = 1
    while i < n:
        sum += (2 ** i * math.factorial(j)) / (5 * 3 ** j)
        i += 1
        j += 1
    return sum
