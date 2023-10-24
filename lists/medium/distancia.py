def distancia(lista_precos) -> float:
    soma_quadrados = 0
    for desejado, venda in lista_precos:
        diferenca = desejado - venda
        soma_quadrados += diferenca ** 2
    return (soma_quadrados / len(lista_precos)) ** 0.5