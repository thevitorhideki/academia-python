def inverte_dicionario(people: dict) -> dict:
    ages = {}

    for name, age in people.items():
        ages.setdefault(age, []).append(name)

    return ages
