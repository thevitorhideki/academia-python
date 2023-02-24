def calcula_troco(purchase: float, paid: float, cash: list):
    change = paid - purchase
    change_list = []
    total_change = []

    # Percorre a lista de trocos e enquanto o troco da compra for maior ou igual o troco do caixa,
    # adiciona o valor do troco na lista "change_list" e diminui o troco
    for value in cash:
        while change >= value:
            change_list.append(value)
            change -= value

    # Percorre a lista de trocos e adiciona na lista do total de troco o numero de notas e o valor delas
    for value in cash:
        count = change_list.count(value)
        if change_list.count(value) > 0:
            if value > 1:
                total_change.append(f"{count} nota(s) de R$ {value}")
            else:
                total_change.append(f"{count} moeda(s) de R$ {value}")

    return total_change


print(calcula_troco(2.25, 1000, [
      100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05]))
