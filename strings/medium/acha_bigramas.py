def acha_bigramas(word: str) -> list:
    bigramas = []

    for i in range(len(word) - 1):
        if word[i:i+2] not in bigramas:
            bigramas.append(word[i:i+2])

    return bigramas
