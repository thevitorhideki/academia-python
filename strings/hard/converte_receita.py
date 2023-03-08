import re


def converte_receita(receipt: dict):
    medidas = {'xícara': 250, 'sopa': 15, 'chá': 5}

    for item, value in receipt.items():
        for medida in medidas:
            if medida in value:
                receipt[item] = str(medidas[medida] *
                                    int(re.sub(r'\D+', '', value))) + ' ml'

    return receipt
