def analise_sentimento(file: str, positive_words: list, negative_words: list) -> list:
    tweet_classification = []

    with open(file, 'r') as tweet:
        content = tweet.readlines()
        content = [x.split() for x in content]
        print(content)

    for tweet in content:
        classification = 0
        for word in tweet:
            if word in positive_words:
                classification += 1
            elif word in negative_words:
                classification -= 1
        if classification > 0:
            tweet_classification.append(1)
        elif classification < 0:
            tweet_classification.append(2)
        else:
            tweet_classification.append(0)

    return tweet_classification


print(analise_sentimento(
    'files/tweet.txt',
    [
        'amor', 'amei', 'lindo', 'sensacional',
        'feliz', 'bom', 'indicar', 'ótimo'
    ],
    [
        'processo', 'problema', 'raiva', 'ódio',
        'procon', 'justiça', 'travou', 'emperrou'
    ]))
