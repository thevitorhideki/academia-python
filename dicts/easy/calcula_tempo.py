from math import sqrt


def calcula_tempo(athletes: dict):
    new_athletes = {}

    for k, v in athletes.items():
        new_athletes[k] = sqrt(100/(v/2))

    return new_athletes


print(calcula_tempo({'joão': 10}))
