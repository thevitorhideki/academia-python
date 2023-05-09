import re


def quanto_tempo(tempos: list) -> str:
    total = {'h': 0, 'm': 0, 's': 0}

    for tempo in tempos:
        tmp = re.sub(r'[^0-9]', ' ', tempo).split()
        tmp2 = re.sub(r'[^a-z]', ' ', tempo).split()
        for i in range(len(tmp)):
            total[tmp2[i]] += int(tmp[i])

    if total['s'] > 59:
        total['m'] += total['s'] // 60
        total['s'] -= 60 * (total['s'] // 60)
    if total['m'] > 59:
        total['h'] += total['m'] // 60
        total['m'] -= 60 * (total['m'] // 60)

    total_str = ''
    for k, v in total.items():
        total_str += f'{v}{k}'

    return total_str
