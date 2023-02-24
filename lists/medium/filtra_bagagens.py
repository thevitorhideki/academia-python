def filtra_bagagens(baggages, max_height, max_width, max_length):
    exceed = 0

    for i in range(len(baggages)):
        if baggages[i][0] > max_height or baggages[i][1] > max_width or baggages[i][2] > max_length:
            exceed += 1

    return exceed
