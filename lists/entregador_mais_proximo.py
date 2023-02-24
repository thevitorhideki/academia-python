from math import sqrt


def entregador_mais_proximo(restaurant, deliverers):
    distance = []

    for i in range(len(deliverers)):
        distance.append(sqrt(
            (deliverers[i][0] - restaurant[0]) ** 2 + (deliverers[i][1] - restaurant[1]) ** 2))

    return(distance.index(min(distance)))
