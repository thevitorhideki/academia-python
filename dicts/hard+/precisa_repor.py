def precisa_repor(materials: dict, rooms: dict):
    replacement = {}

    if len(materials) == 0:
        return replacement
    elif len(rooms) == 0:
        return replacement

    for room, desc in rooms.items():
        for material, level in desc['materiais'].items():
            if material in materials:
                if level < materials[material]['nivel minimo']:
                    replacement.setdefault(materials[material]['responsavel'], []).append(
                        {'sala': room, 'material': material})

    return replacement
