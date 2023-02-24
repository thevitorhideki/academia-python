def quantos_caminhoes(weights):
    trucks = 1
    soma = 0

    for i in weights:
        if soma + i <= 2000:
            soma += i
        else:
            trucks += 1
            soma = 0
            soma += i

    return trucks
