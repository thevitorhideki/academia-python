import math


def altura_do_predio(comprimento_sombra, angulo_sol):
    altura_predio = math.tan(math.radians(angulo_sol)) * comprimento_sombra

    return altura_predio
