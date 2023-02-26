def valor_a_devolver(shelves: dict[dict], cashier: dict[dict], shopping: list[list]) -> float:
    total = 0

    for i in shopping:
        for shelve_k, shelve_v in shelves[i[0]].items():
            for cashier_k, cashier_v in cashier[i[0]].items():
                if shelve_k == i[1] and cashier_k == i[1]:
                    if shelve_v < cashier_v:
                        total += (cashier_v - shelve_v) * i[2]
                        break
    return total
