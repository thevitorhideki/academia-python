def pet_pode_viajar(pet, limit, passages):
    box_dimensions = [x for x in pet[4]]
    limit_dimensions = [x for x in limit[2]]
    pet_count = 0

    if pet[2] + pet[3] >= limit[1]:
        return False
    elif pet[-1] == 'N':
        return False

    for i in range(len(box_dimensions)):
        if box_dimensions[i] > limit_dimensions[i]:
            return False

    if len(passages) >= 1:
        for i in passages:
            if 'pet_cabine' in i[1]:
                pet_count += 1

    if pet_count >= limit[0]:
        return False

    return True


print(pet_pode_viajar(['Totó', 'cachorro', 5.5, 1.0, [20.0, 30.0, 40.0], 'S'], [3, 7.0, [20.0, 35.0, 45.0]], [
    ['1A', []],
    ['5C', ['alergia', 'pet_cabine']],
    ['6D', []],
    ['7A', []],
    ['7A', ['cadeira_rodas']],
    ['9B', ['pet_cabine']]
]))
