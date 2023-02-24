def apurando_votos(candidates: list, votes: list) -> str:
    total_votes = []
    null = 0

    for i in range(len(candidates)):
        total_votes.append(votes.count(candidates[i]))

    for i in votes:
        if i not in candidates:
            null += 1

    if null >= max(total_votes):
        return 'CANCELADA'

    winner = candidates[total_votes.index(max(total_votes))]

    return winner
