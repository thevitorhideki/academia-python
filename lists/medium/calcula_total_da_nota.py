def calcula_total_da_nota(prices, amount):
    total = 0

    for i in range(len(prices)):
        total += prices[i] * amount[i]

    return total
