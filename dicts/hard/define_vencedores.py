def define_vencedores(numbers: list, players: dict):
    player = {name: 0 for name in players}
    winner = []

    for name, player_num in players.items():
        player[name] = sum(1 for num in numbers if num in player_num)

    more_points = max(player.values())
    winner = [name for name, points in player.items() if points == more_points]

    return winner
