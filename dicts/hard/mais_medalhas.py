def mais_medalhas(athletes: list) -> str:
    total_medals = {}

    for athlete in athletes:
        if athlete['nacionalidade'] not in total_medals:
            total_medals[athlete['nacionalidade']] = athlete['ouro']
        else:
            total_medals[athlete['nacionalidade']] += athlete['ouro']

    return max(total_medals, key=lambda x: total_medals[x])
