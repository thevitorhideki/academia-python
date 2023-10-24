def dp_amostral(desejados, media_desejados) -> float:
    soma_quadrados = 0
    for valores in desejados:
        diferenca = valores - media_desejados
        soma_quadrados += diferenca ** 2
    return (soma_quadrados / (len(desejados)-1)) ** 0.5

def distancia(lista_precos) -> float:
    soma_quadrados = 0
    for desejado, venda in lista_precos:
        diferenca = desejado - venda
        soma_quadrados += diferenca ** 2
    return (soma_quadrados / len(lista_precos)) ** 0.5

valor_desejado = input('Valor desejado: ')
lista_precos = []
while valor_desejado != '':
    valor_desejado = float(valor_desejado)
    valor_venda = input('Valor da venda: ')
    if valor_venda == '':
        break
    elif float(valor_desejado) > float(valor_venda):
        print('entradas desconsideradas pois valor desejado maior que o valor da venda, tente novamente!')
    else: 
        valor_venda = float(valor_venda)
        lista_precos.append([valor_desejado, valor_venda])
    valor_desejado = input('Valor desejado: ')

media_desejado = sum([x[0] for x in lista_precos]) / len(lista_precos)
media_venda = sum([x[1] for x in lista_precos]) / len(lista_precos)
media_total = (media_desejado + media_venda) / 2
anomalia = False

if distancia(lista_precos) > 0.05 * media_total:
    anomalia = True

dp_amostral_desejado = dp_amostral([x[0] for x in lista_precos], media_desejado)
dp_amostral_venda = dp_amostral([x[1] for x in lista_precos], media_venda)
print(f'MÉDIA: desejado [{media_desejado:.2f}] venda [{media_venda:.2f}]')
print(f'DESVIO PADRÃO AMOSTRAL: desejado [{dp_amostral_desejado:.2f}] venda [{dp_amostral_venda:.2f}]')
print(f'Anomalia: {"SIM" if anomalia else "NÃO"}')