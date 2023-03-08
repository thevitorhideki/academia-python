def separa_por_inicial(names: dict) -> dict:
    sorted_by_name = {}

    for name in names.values():
        for i in name:
            sorted_by_name.setdefault(i[0], []).append(i)

    return sorted_by_name
