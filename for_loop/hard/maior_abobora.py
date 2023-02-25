def maior_abobora(specie: str, pumpkin: list) -> int:
    index = -1
    size = 0

    for i in range(len(pumpkin)):
        for j in pumpkin[i]:
            if j[1] == specie and size < j[0]:
                index = i
                size = j[0]

    return index


print(maior_abobora('japonesa', [
    [[2.3, 'kabotia']],
    [[6.2, 'kabotia'], [5.5, 'moranga'], [2.5, 'japonesa'], [1.4, 'moranga']],
    [[4.2, 'moranga'], [9.2, 'moranga'], [14.2, 'moranga']],
    [[5.6, 'kabotia'], [16.2, 'kabotia']],
    [[5.5, 'japonesa'], [12.2, 'japonesa'], [12.3, 'japonesa']],
    [[1.2, 'moranga'], [9.2, 'japonesa'], [8.5, 'japonesa']],
]))
