def conserta_teclado(word: str) -> str:
    word = word.lower()
    new_str = ''

    for i in range(len(word)):
        if word[i] != word[i-1]:
            new_str += word[i]

    return new_str.lower()
