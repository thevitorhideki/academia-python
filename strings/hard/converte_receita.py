def converte_receita(receita: dict):
    # Dicionário de unidades de medida em ml
    medidas = {'xícara': 250, 'sopa': 15, 'chá': 5}

    for item, value in receita.items():
        for medida in medidas:
            if medida in value:
                receita[item] = str(medidas[medida] * int(value[:value.find(' ')])) + ' ml'

    return receita
