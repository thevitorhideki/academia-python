def eh_identidade(list):
    if len(list) == len(list[0]):
        for i in range(len(list)):
            for j in range(len(list[i])):
                if list[i][j] == 1 and j != i:
                    return False
                elif 1 not in list[i] or list[i][j] < 0:
                    return False

        return True

    return False
