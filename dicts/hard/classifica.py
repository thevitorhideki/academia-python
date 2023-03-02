import math


def classifica(fishes: dict, fish: list) -> str:
    distance = {x: [] for x in fishes}

    for category, values in fishes.items():
        for i in range(len(values)):
            distance[category].append(math.sqrt((fish[0] - values[i][0]) **
                                                2 + (fish[1] - values[i][1]) ** 2))
        distance[category] = min(distance[category])

    closest = sorted(distance.items(), key=lambda x: x[1])

    return closest[0][0]
