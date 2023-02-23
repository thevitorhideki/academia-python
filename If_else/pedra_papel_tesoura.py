def pedra_papel_tesoura(jogador_1,jogador_2):
    if jogador_1=='pedra' and jogador_2=='tesoura':
        return 'um'
    elif jogador_1=='pedra' and jogador_2=='papel':
        return 'dois'
    elif jogador_1=='pedra' and jogador_2=='pedra':
        return 'empate'
    elif jogador_1=='tesoura' and jogador_2=='papel':
        return 'um'
    elif jogador_1=='tesoura' and jogador_2=='pedra':
        return 'dois'
    elif jogador_1=='tesoura' and jogador_2=='tesoura':
        return 'empate'
    elif jogador_1=='papel' and jogador_2=='pedra':
        return 'um'
    elif jogador_1=='papel' and jogador_2=='tesoura':
        return 'dois'
    elif jogador_1=='papel' and jogador_2=='papel':
        return 'empate'
    else:
        return 'Escolha pedra, papel ou tesoura para jogar'