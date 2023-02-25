def interseccao_valores(dict1: dict, dict2: dict) -> list:
    present_both = []

    for i in dict1.values:
        if i in dict2.values():
            present_both.append(i)

    return present_both
