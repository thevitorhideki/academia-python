def filtra_positivos(numbers):
    new_list = []

    for i in numbers:
        if i > 0:
            new_list.append(i)

    return new_list
