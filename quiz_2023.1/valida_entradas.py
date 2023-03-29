def valida_entradas(lista):
    if len(lista) == 0 or lista[-1] != '=':
        return False
    for i, v in enumerate(lista):
        if i % 2 == 0 and v.isdigit() == False:
            return False
        elif v == '=' and i == len(lista) - 1:
            return True
        elif i % 2 != 0 and v not in ['+', '-', '*', '/', '%', '**', '//']:
            return False
    return True
