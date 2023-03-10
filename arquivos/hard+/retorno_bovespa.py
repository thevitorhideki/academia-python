def retorno_bovespa(initial_date: str, final_date: str) -> float:
    with open('bovespa.csv', 'r') as bov:
        content = bov.read()
        content = content.split('\n')
        content = [x.split(',') for x in content]

    initial_close = 0
    final_close = 0
    for day in content:
        for info in day:
            if initial_date == info:
                initial_close = float(day[4])
            elif final_date == info:
                final_close = float(day[4])

    if initial_close == 0 or final_date == 0:
        return 'sem dados'

    income = (final_close - initial_close) / initial_close
    return income
