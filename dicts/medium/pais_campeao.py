def pais_campeao(countries: dict) -> str:
    golds = {}
    silvers = {}
    bronzes = {}

    for country, medals in countries.items():
        golds[country] = medals.get('ouro', 0)
        silvers[country] = medals.get('prata', 0)
        bronzes[country] = medals.get('bronze', 0)

    winner = sorted(
        golds.items(), key=lambda x: (x[1], silvers[x[0]], bronzes[x[0]]), reverse=True)

    return winner[0][0]
