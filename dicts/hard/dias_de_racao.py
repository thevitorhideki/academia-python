from math import floor


def dias_de_racao(storage: list[dict], pet: dict) -> int:
    days = 0
    if pet['idade'] <= 1:
        pet['idade'] = 'filhote'
    elif pet['idade'] < 8:
        pet['idade'] = 'adulto'
    else:
        pet['idade'] = 'idoso'

    for food in storage:
        if food['porte'] == pet['porte']:
            if food['indicado'] == pet['idade']:
                days += food['qtde']*1000 / pet['gramas_dia']

    return floor(days)
