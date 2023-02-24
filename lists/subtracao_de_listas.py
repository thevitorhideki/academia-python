def subtracao_de_listas(list1, list2):
    new_list = []

    for i in list1:
        if i not in list2:
            new_list.append(i)

    return new_list
