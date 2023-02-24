def calcula_escola(escolas_de_samba: list) -> float:
    nota = 0
    for i in range(len(escolas_de_samba)):
        escolas_de_samba[i].remove(min(escolas_de_samba[i]))
        nota += sum(escolas_de_samba[i])

    return nota
