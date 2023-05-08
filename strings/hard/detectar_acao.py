def detectar_acao(users: dict, stop_words: list) -> dict:
    # Cria uma lista com os nomes dos usuários
    actions = {x: [] for x in users}
    pattern = ['ar', 'er', 'ir', 'or']

    for name, des in users.items():
        for feedback in des.values():
            # Separa as palavras das frases em uma lista
            feedback = feedback.split(' ')

            # Remove as stop_words das frases
            feedback = [x for x in feedback if x not in stop_words]

            for i, value in enumerate(feedback):
                # Verifica se a palavra é a ultima da string e se é um verbo e adiciona no dicionario
                if i == len(feedback) - 1 and value[-2:] in pattern:
                        actions[name].append(value)
                # Verifica se é um verbo e adiciona no dicionário de ações com a próxima palavra
                elif value[-2:] in pattern:
                    actions[name].append(value + ' ' + feedback[i+1])

    return actions
