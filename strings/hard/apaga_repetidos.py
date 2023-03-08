def apaga_repetidos(text: str) -> str:
    new_text = ''
    repeated = []

    for letter in text:
        if letter not in repeated:
            repeated.append(letter)
            new_text += letter
        else:
            new_text += '*'

    return new_text
