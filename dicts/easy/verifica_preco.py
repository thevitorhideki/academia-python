def verifica_preco(title: str, books: dict, colors: dict):
    for k, v in books.items():
        if k == title:
            return colors[v]
