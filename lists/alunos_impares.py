def alunos_impares(alunos):
    impares = []
    pares = []
    for i in range(len(alunos)):
        if i % 2 == 0:
            pares.append(alunos[i])
        else:
            impares.append(alunos[i])

    return impares
