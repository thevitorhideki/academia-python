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
