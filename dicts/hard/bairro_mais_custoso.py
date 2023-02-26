def total_do_semestre_por_bairro(expenses: dict) -> dict:
    last_six_months = {k: sum(v[-6:]) for k, v in expenses.items()}

    return last_six_months


def bairro_mais_custoso(districts: dict) -> str:
    district_expenses = total_do_semestre_por_bairro(districts)

    return max(district_expenses, key=lambda x: district_expenses[x])
