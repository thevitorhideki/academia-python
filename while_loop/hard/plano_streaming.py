plano = input("Qual é o seu plano? ")

series = {
    'novo': [
        'the circle', 'mad men'
    ],
    'padrao': [
        'stranger things', 'friends', 'the circle', 'mad men'
    ],
    'premium': [
        'stranger things', 'friends', 'the circle', 'mad men', 'brasileirao', 'champions'
    ]
}

while True:
    serie = input("Qual serie quer assistir? ")

    for i in series:
        if plano == i:
            if serie in series[i]:
                print('Ok, reproduzindo!')
                if plano == 'novo':
                    print('Num oferecimento de DesSoft!')
            elif serie == 'sair':
                break
            elif serie not in series['premium']:
                print('Serie inexistente!')
            else:
                print('Precisa comprar novo plano!')

    if serie == 'sair':
        print('Ok, tchau!')
        break

