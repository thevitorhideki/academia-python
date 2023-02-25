def compras_da_semana(receipts: dict, plates: list):
    ingredient = {}

    for i in plates:
        for name, value in receipts.items():
            if name == i:
                for k, v in value.items():
                    if k not in ingredient:
                        ingredient[k] = v
                    else:
                        ingredient[k] += v

    return ingredient
