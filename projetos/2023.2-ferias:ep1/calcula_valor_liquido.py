def calcula_valor_liquido(valor: float, origem: str) -> float:
    if origem == 'pyfood':
        return valor * 0.70
    elif origem == 'whatsapp':
        return (valor * 0.985) - 7.5
