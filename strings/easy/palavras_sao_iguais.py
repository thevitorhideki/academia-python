def palavras_sao_iguais(word: str) -> bool:
    left, x, right = word.partition('-')

    return left == right
