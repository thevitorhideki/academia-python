def total_centro_custo(expenses: dict) -> dict:
    cost_center = {}

    for expense in expenses.values():
        if expense['centro de custo'] not in cost_center:
            cost_center[expense['centro de custo']] = expense['valor']
        else:
            cost_center[expense['centro de custo']] += expense['valor']

    return cost_center
