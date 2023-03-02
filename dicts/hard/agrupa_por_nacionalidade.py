def agrupa_por_nacionalidade(athletes: dict) -> dict:
    countries = {}

    for name, desc in athletes.items():
        countries.setdefault(desc['nacionalidade'], []).append(name)

    return countries
