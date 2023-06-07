def calcula_premiacao(arrecadacao: int, sorteados: list, dados: dict) -> dict:
    acertos = {nome: 0 for nome in dados.keys()}
    acertos_totais = {
        '6 acertos': {
            'ganhadores': 0, 
            'premio por pessoa': 0
        }, 
        '5 acertos': {
            'ganhadores': 0, 
            'premio por pessoa': 0
        }, 
        '4 acertos': {
            'ganhadores': 0, 
            'premio por pessoa': 0
        }
    }
    premiacao = arrecadacao * 0.455
    premio_60 = premiacao * 0.6
    premio_20 = premiacao * 0.2
    
    # Conta quantos acertos
    for nome, numeros in dados.items():
        for numero in numeros:
            if numero in sorteados:
                acertos[nome] += 1
                
    for acertos in acertos.values():
        if acertos == 4:
            acertos_totais['4 acertos']['ganhadores'] += 1
        elif acertos == 5:
            acertos_totais['5 acertos']['ganhadores'] += 1
        elif acertos == 6:
            acertos_totais['6 acertos']['ganhadores'] += 1
        
    for acertos, dados in acertos_totais.items():
        if acertos == '6 acertos' and dados['ganhadores'] != 0:
            acertos_totais[acertos]['premio por pessoa'] = premio_60 / acertos_totais[acertos]['ganhadores']
        elif acertos != '6 acertos' and dados['ganhadores'] != 0:
            acertos_totais[acertos]['premio por pessoa'] = premio_20 / acertos_totais[acertos]['ganhadores']
    
    return acertos_totais
        