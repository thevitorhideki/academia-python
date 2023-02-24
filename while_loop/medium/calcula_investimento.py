def calcula_investimento(investimento, tempo, papel):
    CDB = 1.0130
    LCI = 1.0160
    LCA = 1.0145
    
    for i in range(1, tempo+1):
        if papel == 'CDB':
            investimento *= CDB
            if i % 6 == 0:
                investimento *= 1.012
        elif papel == 'LCI':
            investimento *= LCI
        elif papel == 'LCA':
            investimento *= LCA
            if i % 4 == 0:
                investimento *= 1.01
    return investimento 
