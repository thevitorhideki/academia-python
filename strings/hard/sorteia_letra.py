from random import choice


def sorteia_letra(text: str, restriction: list) -> str:
    restriction += ['.', ',', '-', ';', ' ']
    text = [char for char in text.lower() if char not in restriction]

    return '' if not text else choice(text)
