def bussola(x_monstro, y_monstro, x_jogador, y_jogador):
    if x_monstro == x_jogador and y_monstro == y_jogador:
        return 'achou'
    elif abs(x_monstro - x_jogador) == abs(y_monstro - y_jogador):
        return 'norte' if y_monstro > y_jogador else 'sul'
    elif x_monstro == x_jogador:
        return 'norte' if y_monstro > y_jogador else 'sul'
    elif y_monstro == y_jogador:
        return 'oeste' if x_monstro > x_jogador else 'leste'

    elif abs(x_monstro - x_jogador) > abs(y_monstro - y_jogador):
        return 'norte' if y_monstro > y_jogador else 'sul'
    elif abs(x_monstro - x_jogador) < abs(y_monstro - y_jogador):
        return 'oeste' if x_monstro > x_jogador else 'leste'
