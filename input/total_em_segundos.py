i_dias = int(input(("Digite uma quantidade de dias: ")))
i_horas = int(input(("Digite uma quantidade de horas: ")))
i_minutos = int(input(("Digite uma quantidade de minutos: ")))
i_segundos = int(input(("Digite uma quantidade de segundos: ")))

def calcular_tempo(dias, horas, minutos, segundos):
    dias = dias * 24 * 60 * 60
    horas = horas * 60 * 60
    minutos = minutos * 60
    
    return dias + horas + minutos + segundos

print(calcular_tempo(i_dias, i_horas, i_minutos, i_segundos))
