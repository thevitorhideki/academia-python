def mais_populoso(brazil_states: dict):
    population = {}

    for state, cities in brazil_states.items():
        for value in cities.values():
            if state not in population:
                population[state] = value
            else:
                population[state] += value

    most_populous = sorted(population.items(), key=lambda x: -x[1])

    return most_populous[0][0]
