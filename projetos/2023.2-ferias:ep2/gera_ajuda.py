from random import randint, choice

def gera_ajuda(questao: dict):
    incorretas = [v for k, v in questao['opcoes'].items() if k != questao['correta']]
    
    qnt = randint(1,2)

    if qnt == 1:
        return f'DICA:\nOpções certamente erradas: {choice(incorretas)}'
    else:
        return f'DICA:\nOpções certamente erradas: {choice(incorretas)} | {choice(incorretas)}'
