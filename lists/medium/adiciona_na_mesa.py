def adiciona_na_mesa(piece, table):
    new_table = table[::]

    if len(table) == 0:
        new_table.append(piece)
    elif len(table) == 1:
        if table[0][0] == piece[0]:
            new_table.insert(0, piece[::-1])
        elif table[0][0] == piece[1]:
            new_table.insert(0, piece)
        elif table[0][1] == piece[0]:
            new_table.append(piece)
        elif table[0][1] == piece[1]:
            new_table.append(piece[::-1])
    elif table[0][0] == piece[0]:
        new_table.insert(0, piece[::-1])
    elif table[0][0] == piece[1]:
        new_table.insert(0, piece)
    elif table[-1][1] == piece[0]:
        new_table.append(piece)
    elif table[-1][1] == piece[1]:
        new_table.append(piece[::-1])

    return new_table
