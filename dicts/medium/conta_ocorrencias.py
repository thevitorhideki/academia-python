def conta_ocorrencias(words: list):
    occurrences = {}

    for i in words:
        if i not in occurrences:
            occurrences[i] = 1
        else:
            occurrences[i] += 1

    return occurrences
