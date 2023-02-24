from math import floor


def contabilizar(volume: int, bottle_filled: list) -> int:
    total_volume = sum([x[1] * x[0] for x in bottle_filled])
    total_bottles = floor(total_volume/volume)

    return total_bottles


print(contabilizar(500, [[750, 4], [500, 2]]))
