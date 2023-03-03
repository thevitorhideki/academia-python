def repassa_investimentos(companies: dict, investments: dict, company: str, market_value: float, percent: float):
    distribution = market_value * percent / 100
    for name, percent in companies[company]['associados'].items():
        if name not in companies:
            if name not in investments:
                investments[name] = distribution * percent / 100
            else:
                investments[name] += distribution * percent / 100
        else:
            repassa_investimentos(companies, investments,
                                  name, distribution, percent)


def soma_investimento(companies: dict) -> dict:
    investments = {}

    # Soma os investimentos das pessoas físicas
    for company_desc in companies.values():
        market_value = company_desc['valor de mercado']
        for name, percent in company_desc['associados'].items():
            if name not in companies:
                if name not in investments:
                    investments[name] = market_value * percent / 100
                else:
                    investments[name] += market_value * percent / 100
            else:
                repassa_investimentos(
                    companies, investments, name, market_value, percent)

    return investments
