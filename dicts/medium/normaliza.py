def normaliza(continents: dict) -> dict:
    countries = {}

    for country in continents.values():
        for k, v in country.items():
            countries[k] = v

    return countries
