def esta_na_lista(country, countries):
    return True if [x for x in countries if country in x] else False
