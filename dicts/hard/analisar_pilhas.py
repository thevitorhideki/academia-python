def analisar_pilhas(brands_models: dict, batteries: list) -> list:
    status = []

    if len(brands_models) == 0:
        for i in range(len(batteries)):
            status.append('E')
    else:
        for i in batteries:
            if i[0] not in brands_models:
                status.append('E')
            elif i[1] not in brands_models[i[0]]:
                status.append('E')
            else:
                model = brands_models[i[0]][i[1]]
                limit = model['volts'] * (1 - model['limite'])
                if i[2] >= limit:
                    status.append('N')
                elif i[2] < limit:
                    if model['recarregavel'] == False:
                        status.append('D')
                    elif model['recarregavel'] == True:
                        status.append('R')

    return status


print(analisar_pilhas(
    {
        "duracell": {
            "duramax": {
                "capacidade": "3000 mah",
                "volts": 9,
                "limite": 0.05,
                "recarregavel": True
            }
        },
        "rayovac": {
            "amarelinha": {
                "capacidade": "2700 mah",
                "volts": 1.4,
                "limite": 0.15,
                "recarregavel": False
            },
            "gold": {
                "capacidade": "3500 mah",
                "volts": 6.0,
                "limite": 0.1,
                "recarregavel": True
            }
        }
    },
    [
        ['duracell', 'duramax', 8.0],
        ['duracell', 'duramax', 8.8],
        ['elgin', 'max', 1.2],
        ['duracell', 'alcalina', 1.21],
        ['rayovac', 'amarelinha', 1.01],
        ['rayovac', 'amarelinha', 1.38],
        ['rayovac', 'gold', 5.0],
        ['rayovac', 'gold', 6.2]
    ]))
