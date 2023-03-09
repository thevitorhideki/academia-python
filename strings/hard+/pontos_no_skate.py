import re


def pontos_no_skate(tricks: dict, performances: dict):
    tricks = {k.lower(): int(v[:v.index(' ')]) for k, v in tricks.items()}

    results = {
        name: {
            'qtde manobras': 0, 'total pontos': 0
        }
        for name in performances}

    for name, desc in performances.items():
        for phrase in desc['frases']:
            phrase = phrase.lower()
            phrase = re.sub('[!?,;.:\)\}\]\(\[\{]', '', phrase).split()
            for trick, value in tricks.items():
                for x in phrase:
                    if trick == x:
                        results[name]['qtde manobras'] += 1
                        results[name]['total pontos'] += value

    return results
