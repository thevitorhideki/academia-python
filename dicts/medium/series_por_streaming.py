def series_por_streaming(platforms, actors, titles):
    series = {}

    for i in range(len(platforms)):
        serie = dict(performer=actors[i], title=titles[i])
        if platforms[i] not in series:
            series[platforms[i]] = [serie]
        else:
            series[platforms[i]].append(serie)

    return series
