from math import sqrt


def calcula_tempo(athletes: dict):
    new_athletes = {}

    for k, v in athletes.items():
        new_athletes[k] = sqrt(100/(v/2))

    return new_athletes


athletes = {}
while True:
    name = input("Digite o nome do atleta: ")
    if name == 'sair':
        break

    acceleration = float(input("Digite a aceleração: "))

    athletes[name] = acceleration

athletes_time = calcula_tempo(athletes)
lowest_time = min(athletes_time.values())

for k, v in athletes_time.items():
    if v == lowest_time:
        print(f"O vencedor é {k} com tempo de conclusão de {v} s")
