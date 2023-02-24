while True:
    novo_input = input("Digite algo: ")
    if novo_input == 'bom dia':
        print("Bom dia")
    elif novo_input == 'oi':
        print('Olá!')
    elif novo_input == 'site':
        print("Acesse https://insper.edu.br")
    elif novo_input == 'blackboard':
        print("Lá temos materiais, notas e muito mais!")
    elif novo_input == 'tchau' or novo_input == 'encerrar':
        print("Até logo")
        break
    else:
        print('Não sei como te ajudar!')
