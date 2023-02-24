def produz_um_dois_insper(start, stop, step):
    list = []
    for i in range(start, stop + 1):
        if i % step == 0:
            list.append('Insper')
        else:
            list.append(i)

    return list
