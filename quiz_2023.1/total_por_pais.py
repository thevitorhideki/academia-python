def total_por_pais(poluicao: dict) -> dict:
    poluicao_por_pais = {}

    for pais, cidade in poluicao.items():
        for index in cidade.values():
            if pais not in poluicao_por_pais:
                poluicao_por_pais[pais] = abs(index)
            else:
                poluicao_por_pais[pais] += abs(index)

    return poluicao_por_pais
