def seleciona_candidatos(candidates, criteria):
    selected = []

    for i in range(len(candidates)):
        if len(candidates[i][2]) == 3:
            if candidates[i][2][0] >= criteria[0] and candidates[i][2][1] >= criteria[1] and candidates[i][2][2] >= criteria[2]:
                selected.append(candidates[i][:-1])

    return selected
