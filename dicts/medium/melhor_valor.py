def melhor_valor(parts: list, inventory: list[dict]) -> float:
    total = 0
    sorted_inventory = sorted(inventory, key=lambda x: x['valor'])

    for i in parts:
        for j in sorted_inventory:
            if i in j['equivalente']:
                total += j['valor']
                break
            elif i == j['serial']:
                total += j['valor']
                break

    return total


print(melhor_valor(['X1D', 'A3B'], [
    {'serial': 'A3B', 'valor': 198.7, 'equivalente': []},
    {'serial': 'XP2', 'valor': 190.9, 'equivalente': ['Z3Z', 'A3B']},
    {'serial': 'XP1', 'valor':   5.1,
        'equivalente': ['TH5', 'TH6', 'X3D', 'X1D']}
]))
