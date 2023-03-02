def calcula_dano(player: list) -> int:
    damage = player['força']

    for equipments in player['equipamentos']:
        damage += equipments['força']

    return damage
