def esta_na_lista(country, countries):
    for i in countries:
        if country in i:
            return True
    return False
