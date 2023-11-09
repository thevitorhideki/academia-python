def inidica_posicao(sorteada: str, especulada: str) -> list:
    posicoes = []
    sorteada = sorteada.lower()
    especulada = especulada.lower()

    if len(sorteada) != len(especulada):
        return []

    for i, letra in enumerate(especulada):
        if letra == sorteada[i]:
            posicoes.append(0)
        elif letra != sorteada[i] and letra in sorteada:
            posicoes.append(1)
        else:
            posicoes.append(2)

    return posicoes
