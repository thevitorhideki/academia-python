import random
import math


def sorteia_posicao_do_monstro(largura, altura):
    return random.randint(0, largura-1), random.randint(0, altura-1)


def sorteia_posicao_do_jogador(largura, altura, x_monstro, y_monstro):
    # Sorteando posição inicial do jogador no tabuleiro
    # Faz validação para que nÃ£o seja sorteada a mesma posição em que o monstro se encontra
    sorteia_pos = True
    while sorteia_pos:
        x_jogador = random.randint(0, largura-1)
        y_jogador = random.randint(0, altura-1)
        if x_jogador != x_monstro or y_jogador != y_monstro:
            sorteia_pos = False
    return x_jogador, y_jogador


def sorteia_posicao_da_porta(largura, altura, x_monstro, y_monstro, x_jogador, y_jogador):
    # Sorteando posição inicial da porta no tabuleiro
    # Faz uma validação para que nÃ£o seja sorteada a mesma posição em que o monstro e a porta se encontram
    sorteia_pos = True
    while sorteia_pos:
        x_porta = random.randint(0, largura-1)
        y_porta = random.randint(0, altura-1)
        if (x_porta != x_monstro or y_porta != y_monstro) and (x_porta != x_jogador or y_porta != y_jogador):
            sorteia_pos = False
    return x_porta, y_porta


def dica(x_monstro, y_monstro, x_jogador, y_jogador):
    distancia = math.sqrt((x_jogador - x_monstro) **
                          2 + (y_jogador-y_monstro)**2)
    if distancia <= 2:
        return 'quente'
    elif distancia <= 3:
        return 'morno'
    elif distancia <= 4:
        return 'fresco'
    else:
        return 'frio'


def imprime_tabuleiro(x_monstro, y_monstro, x_jogador, y_jogador, x_porta, y_porta, largura, altura, debug):
    tabuleiro = ''
    linha1 = f"   {'  '.join([f'{i}' for i in range(largura)])}"
    tabuleiro += f'{linha1}\n'
    tabuleiro += f'{"_"*len(linha1)}\n'

    for y in range(altura):
        linha = f'{y}| '
        for x in range(largura):
            if x == x_jogador and y == y_jogador:
                linha += f'J  '
            elif x == x_monstro and y == y_monstro and debug:
                linha += f'M  '
            elif x == x_porta and y == y_porta and debug:
                linha += f'P  '
            else:
                linha += f'_  '

        tabuleiro += f"{linha}\n"
    return tabuleiro


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


# Largura e altura do tabuleiro
largura = 8
altura = 8

# Sorteia posição do monstro
x_monstro, y_monstro = sorteia_posicao_do_monstro(largura, altura)

# Sorteia posição do Jogador
x_jogador, y_jogador = sorteia_posicao_do_jogador(
    largura, altura, x_monstro, y_monstro)

# Sorteia posição da Porta
x_porta, y_porta = sorteia_posicao_da_porta(
    largura, altura, x_monstro, y_monstro, x_jogador, y_jogador)

# ---------------------------------------------------------- #

jogando = True
debug = False  # Com o debug igual a True a posição do monstro e da porta são visíveis
while jogando:

    tabuleiro = imprime_tabuleiro(
        x_monstro, y_monstro, x_jogador, y_jogador, x_porta, y_porta, largura, altura, debug)
    print(tabuleiro)

    while True:
        move = input('Qual direção você deseja andar? ')

        if move in ['w', 'a', 's', 'd']:
            print('Entrada válida')
            break
        else:
            print('Entrada do jogador inválida!')
            print('Você deve digitar a/s/d/w!')

    if move == 'w':
        y_jogador -= 1
    elif move == 'a':
        x_jogador -= 1
    elif move == 's':
        y_jogador += 1
    elif move == 'd':
        x_jogador += 1

    print(f'{x_jogador, y_jogador}')

    if x_jogador == x_porta and y_jogador == y_porta:
        print('Achou a porta!')
        jogando = False
    else:
        move_monstro = bussola(x_monstro, y_monstro, x_jogador, y_jogador)

        if move_monstro == 'norte':
            y_monstro -= 1
        elif move_monstro == 'sul':
            y_monstro += 1
        elif move_monstro == 'oeste':
            x_monstro -= 1
        elif move_monstro == 'leste':
            x_monstro += 1

        print(f'{x_monstro, y_monstro}')

        if x_monstro == x_jogador and y_monstro == y_jogador:
            print('O monstro te achou!')
            jogando = False
        else:
            print(dica(x_monstro, y_monstro, x_jogador, y_jogador))
