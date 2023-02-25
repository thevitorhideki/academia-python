def primeiras_ocorrencias(name: str) -> dict:
    str_occurrence = {}

    for i in range(len(name)):
        if name[i] not in str_occurrence:
            str_occurrence[name[i]] = i

    return str_occurrence
