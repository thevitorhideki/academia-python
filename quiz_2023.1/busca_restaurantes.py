def busca_restaurantes(restaurantes: list, categoria: str, valor: str) -> list:
    filtrados = []

    for restaurante in restaurantes:
        nome = restaurante[0]
        if categoria == 'culinaria':
            if restaurante[1] == valor:
                filtrados.append(nome)
        elif categoria == 'ambiente':
            if restaurante[2] == valor:
                filtrados.append(nome)
        elif categoria == 'preco':
            if restaurante[3] <= valor:
                filtrados.append(nome)

    return filtrados
