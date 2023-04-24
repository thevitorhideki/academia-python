def mais_lancamentos(series, ano):
    plataformas = {}

    for serie in series:
        plataformas.setdefault(serie['plataforma'], []).append(
            serie['ano_estreia'])
    lancamentos = {i: 0 for i in plataformas}

    for plataforma, anos in plataformas.items():
        lancamentos[plataforma] += anos.count(ano)

    max_lancamentos = max(lancamentos.values())
    max_lancamentos_plataformas = []

    for p, v in lancamentos.items():
        if v == max_lancamentos and max_lancamentos != 0:
            max_lancamentos_plataformas.append(p)

    return max_lancamentos_plataformas

