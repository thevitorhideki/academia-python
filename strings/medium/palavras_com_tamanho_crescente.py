def palavras_com_tamanho_crescente(words: list):
    size = 0

    for i in words:
        if len(i) > size:
            size = len(i)
        elif len(i) <= size:
            return False

    return True
