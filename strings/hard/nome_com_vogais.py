import re


def nomes_com_vogais(names: list) -> list:
    pattern = '^[AEIOU]'
    vowels = 0
    consonants = 0

    for name in names:
        if len(re.findall(pattern, name)) == 1:
            vowels += 1
        else:
            consonants += 1

    return [vowels, consonants]


print(nomes_com_vogais(["André", "Carlos", "João", "Otavio", "Thiago"]))
