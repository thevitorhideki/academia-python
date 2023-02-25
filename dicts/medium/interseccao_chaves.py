def interseccao_chaves(dict1: dict, dict2: dict) -> list:
    present_both = []

    for i in dict1:
        if i in dict2.keys():
            present_both.append(i)

    return present_both
