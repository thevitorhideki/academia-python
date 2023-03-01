def calcula_media(athletes: dict, country: str) -> float:
    ages = {}

    for v in athletes.values():
        ages.setdefault(v['nacionalidade'], []).append(v['idade'])

    for k, age in ages.items():
        ages[k] = sum(age) / len(age)

    return ages[country]
