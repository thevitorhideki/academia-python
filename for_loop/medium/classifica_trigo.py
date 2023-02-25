def classifica_trigo(load: list[int]) -> list[str]:
    type = []

    for i in load:
        if i <= 2:
            type.append('T1')
        elif i <= 3:
            type.append('T2')
        elif i <= 7:
            type.append('T3')
        else:
            type.append('FT')

    return type
