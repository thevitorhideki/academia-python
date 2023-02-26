def promocao_viagens(destinations: dict) -> dict:
    destinations_discount = {}

    for k, v in destinations.items():
        destinations_discount[k] = v[1] * (1 - (v[0] / 10))

    return destinations_discount
