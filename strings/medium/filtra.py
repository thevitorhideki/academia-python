def filtra(palavras: list, letras: int) -> list:
    filtradas = []

    for palavra in palavras:
        if len(palavra) == letras and palavra.lower() not in filtradas:
            filtradas.append(palavra.lower())

    return filtradas
