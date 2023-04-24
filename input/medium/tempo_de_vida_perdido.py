import math

cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("A quantos anos você fuma? "))


def tempo_de_vida_perdido(cigarros, anos):
    cigarros_por_ano = cigarros * 365
    total_cigarros = cigarros_por_ano * anos

    tempo_perdido_minutos = total_cigarros * 10
    tempo_perdido_dias = tempo_perdido_minutos / 60 / 24

    return tempo_perdido_dias


print(tempo_de_vida_perdido(cigarros_por_dia, anos))
