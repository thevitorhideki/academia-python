def PiWallis(n):
    pi = 1
    count = 1
    i = 2
    j = 1

    while count <= n:

        if count % 2 == 0:
            pi *= (j / i)
        else:
            pi *= (i / j)

        i += 1
        j += 1
        count += 1

    return pi * 2

