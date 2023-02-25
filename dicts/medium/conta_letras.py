def conta_letras(name: str) -> dict:
    occurrence = {}

    for i in range(len(name)):
        if name[i] not in occurrence:
            occurrence[name[i]] = 1
        else:
            occurrence[name[i]] += 1

    return occurrence
