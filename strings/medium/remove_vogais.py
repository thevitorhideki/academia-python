import re


def remove_vogais(word: str):
    pattern = '[A,E,I,O,U]'
    return re.sub(pattern, '', word, flags=re.IGNORECASE)
