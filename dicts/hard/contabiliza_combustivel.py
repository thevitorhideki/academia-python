def contabiliza_combustivel(fuel: dict) -> dict:
    mean_price = {}

    for value in fuel.values():
        mean_price.setdefault(
            value['tipo'], {
                'total litros': 0, 'custo por litro': 0
            }
        )

        mean_price[value['tipo']]['total litros'] += value['litros']
        mean_price[value['tipo']]['custo por litro'] += value['custo']

    for v in mean_price.values():
        v['custo por litro'] /= v['total litros']

    return mean_price
