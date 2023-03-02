def apura_area(votes: list, parties: list):
    votes_per_area = {}

    for desc in votes:
        area = desc['area']
        votes_per_area.setdefault(area, {'nulos': 0, 'brancos': 0})
        for party, candidates in parties.items():
            for candidate in candidates:
                if candidate in desc['candidatos']:
                    if party not in votes_per_area[area]:
                        votes_per_area[area][party] = desc['candidatos'][candidate]
                    else:
                        votes_per_area[area][party] += desc['candidatos'][candidate]
        votes_per_area[area]['nulos'] += desc['candidatos']['nulos']
        votes_per_area[area]['brancos'] += desc['candidatos']['brancos']
    return votes_per_area
