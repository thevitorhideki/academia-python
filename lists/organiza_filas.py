def organiza_filas(subscribes: list[list[str, int]]) -> list[list[str]]:
    queue = [[], [], [], []]

    for i in subscribes:
        if i[1] <= 20:
            queue[0].append(i[0])
        elif i[1] <= 40:
            queue[1].append(i[0])
        elif i[1] <= 60:
            queue[2].append(i[0])
        else:
            queue[3].append(i[0])

    return queue
