def total_do_semestre_por_bairro(expenses: dict) -> dict:
    last_six_months = {k: sum(v[-6:]) for k, v in expenses.items()}

    return last_six_months
