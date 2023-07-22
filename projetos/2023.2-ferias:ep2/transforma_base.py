def transforma_base(questoes: list) -> dict:
    questoes_por_nivel = {}

    for questao in questoes:
        nivel = questao['nivel']

        questoes_por_nivel.setdefault(nivel, []).append(questao)

    return questoes_por_nivel
