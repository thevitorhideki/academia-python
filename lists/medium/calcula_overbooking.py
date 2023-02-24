def calcula_overbooking(max, passengers):
    extra_passengers = 0

    for i in passengers:
        if i > max:
            extra_passengers += i - max

    return extra_passengers
