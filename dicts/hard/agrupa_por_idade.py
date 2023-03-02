def agrupa_por_idade(people: dict) -> dict:
    age_grupo = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}

    for name, age in people.items():
        if age <= 11:
            age_grupo['criança'].append(name)
        elif age <= 17:
            age_grupo['adolescente'].append(name)
        elif age <= 59:
            age_grupo['adulto'].append(name)
        else:
            age_grupo['idoso'].append(name)

    return age_grupo
