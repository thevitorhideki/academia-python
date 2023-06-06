import re


def predizer_lingua(languages: dict, text: str) -> dict:
    guess = {x: 0.0 for x in languages}
    
    if len(text) == 0:
        guess['palpite'] = 'DESCONHECIDA'
        return guess
    elif len(languages) == 0:
        return {'palpite': 'DESCONHECIDA'}
    
    text = re.sub('[!?,;.:\)\}\]\(\[\{]', '', text).lower().split()
    one_percent = 1 / len(text)

    for lang, words in languages.items():
        for word in words:
            for text_word in text:
                if word == text_word:
                    guess[lang] += one_percent

    if len(guess) == 0:
        return guess

    guess['palpite'] = max(guess, key=lambda x: guess[x])
    return guess
