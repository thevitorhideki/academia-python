def contabiliza(donations: dict) -> dict:
    items = {}

    for values in donations.values():
        for item in values:
            amount = int(item[:item.find(' ')])
            product = item[item.find(' ')+1:]
            if product not in items:
                items[product] = amount
            else:
                items[product] += amount

    return items
