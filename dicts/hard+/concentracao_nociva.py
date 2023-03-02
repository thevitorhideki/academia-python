def concentracao_nociva(atmosphere: list) -> dict:
    gases = {}
    total = 0

    for i in atmosphere:
        for j in i:
            for gas in j:
                if gas not in gases:
                    gases[gas] = 1
                else:
                    gases[gas] += 1
                total += 1

    toxic = {}
    if 'O' not in gases:
        toxic['O'] = 0.0
    for k, v in gases.items():
        v = v / total * 100
        gases[k] = v
        if k == 'O' and v <= 20:
            toxic[k] = v
        elif k == 'N' and v >= 70:
            toxic[k] = v
        elif k != 'O' and k != 'N' and v > 2:
            toxic[k] = v

    return toxic
