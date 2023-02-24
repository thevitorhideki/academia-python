valor = float(input("Digite o valor da conta: "))

def dez_porcento(valor):
    valor += valor * 10 / 100
    return valor

print(f"Valor da conta com 10%: R${round(dez_porcento(valor), 2)}")
