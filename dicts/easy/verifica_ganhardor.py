def verifica_ganhador(game: dict):
    for k, v in game.items():
        if len(v) == 0:
            return k

    return -1
