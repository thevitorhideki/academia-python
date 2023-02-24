def adiciona_em_ordem(country: str, distance: int, countries: list[list[str, int]]) -> list[list[str, int]]:
    countries.append([country, distance])

    for i in range(len(countries)):
        countries[i] = countries[i][::-1]
    countries = sorted(countries)

    for i in range(len(countries)):
        countries[i] = countries[i][::-1]

    return countries
