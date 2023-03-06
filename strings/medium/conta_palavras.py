import re


def conta_palavras(word: str) -> dict:
    words = {}
    if len(word) == 0:
        return words
    word = word.lower()
    word = re.sub('[?!.,]', '', word).split(' ')

    for i in word:
        if i not in words:
            words[i] = 1
        else:
            words[i] += 1

    return words


print(conta_palavras(""))
