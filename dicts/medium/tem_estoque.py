def tem_estoque(peaces: dict, inventory: dict):
    for k1, v1 in inventory.items():
        for k2, v2 in peaces.items():
            if k2 == k1 and v2 > v1:
                return False
            elif k2 not in inventory.keys():
                return False

    return True
