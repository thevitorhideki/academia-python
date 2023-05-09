import re


def analise_morfologica(texto):
    analise = {'adverbio': 0.00, 'conjuncao': 0.00,
               'outras': 0.00, 'preposicao': 0.00}

    if len(texto) == 0:
        analise['adverbio'] = f'{analise["adverbio"]:.2f}' + '%'
        analise['preposicao'] = f"{analise['preposicao']:.2f}" + '%'
        analise['conjuncao'] = f"{analise['conjuncao']:.2f}" + '%'
        analise['outras'] = f"{analise['outras']:.2f}" + '%'

        return analise

    adverbios = ['sim', 'não', 'jamais', 'nunca', 'abaixo', 'acima', 'adentro', 'adiante', 'afora', 'aí', 'além', 'aqui', 'atrás', 'dentro', 'embaixo', 'externamente', 'lá', 'longe', 'perto', 'afinal', 'agora', 'amanhã', 'antes', 'ontem', 'breve', 'cedo', 'constantemente', 'depois', 'enfim', 'hoje',
                 'imediatamente', 'jamais', 'nunca', 'sempre', 'outrora', 'primeiramente', 'tarde', 'provisoriamente', 'sucessivamente', 'já', 'possivelmente', 'provavelmente', 'talvez', 'bastante', 'demais', 'mais', 'menos', 'bem', 'muito', 'quanto', 'quão', 'quase', 'tanto', 'pouco', 'demasiado', 'imenso']
    preposicoes = ['à', 'ante', 'após', 'até', 'com', 'contra', 'de', 'desde',
                   'em', 'entre', 'para', 'per', 'perante', 'por', 'sem', 'sob', 'sobre', 'trás']
    conjuncoes = ['e', 'mas', 'ou', 'pois', 'que', 'como', 'quanto']

    texto = texto.lower()
    texto_limpo = re.sub(r'[!?:,.;\s]', ' ', texto).split()
    percentual = 1 / len(texto_limpo)

    for palavra in texto_limpo:
        if palavra in adverbios:
            analise['adverbio'] += percentual * 100
        elif palavra in conjuncoes:
            analise['conjuncao'] += percentual * 100
        elif palavra in preposicoes:
            analise['preposicao'] += percentual * 100
        else:
            analise['outras'] += percentual * 100

    analise['adverbio'] = f'{analise["adverbio"]:.2f}' + '%'
    analise['preposicao'] = f"{analise['preposicao']:.2f}" + '%'
    analise['conjuncao'] = f"{analise['conjuncao']:.2f}" + '%'
    analise['outras'] = f"{analise['outras']:.2f}" + '%'

    return analise
