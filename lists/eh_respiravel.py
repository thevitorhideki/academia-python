def eh_respiravel(gases: list[list[str]]) -> bool:
    oxygen = 0
    total = sum([len(x) for x in gases])

    for i in gases:
        for j in i:
            if 'O' in j:
                oxygen += 1

    if oxygen/total >= 0.2:
        return True
    return False


print(eh_respiravel([
    ['O', 'N', 'He', 'Rn'],
    ['Ar', 'O', 'He', 'N'],
    ['Uuo', 'O', 'O', 'O'],
    ['O', 'O', 'N', 'O']
]))
