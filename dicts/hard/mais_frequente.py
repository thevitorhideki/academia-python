def mais_frequente(words: list) -> str:
    count = {}

    for i in words:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    return max(count, key=lambda x: count[x])


print(mais_frequente(['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']))
