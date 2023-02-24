def classifica_pedido(valor, dias_atraso, tamanho, avarias, capital):
    if valor <= 1000:
        if dias_atraso <= 1:
            if valor <= 150:
                if avarias == 'n' or avarias == 'N':
                    return 'normal'
                else:
                    return 'reclamacao'
            else:
                return 'reclamacao'
        else:
            return 'reclamacao'
    else:
        if dias_atraso <= 10:
            if avarias == 'n' or avarias == 'N':
                if valor <= 10000:
                    if valor <= 5000:
                        if capital == 'n' or capital == 'N':
                            return 'normal'
                        else:
                            if tamanho == 'p' or tamanho == 'P':
                                return 'reclamacao'
                            else:
                                return 'normal'
                    else:
                        return 'reclamacao'
                else:
                    return 'justica'
            else:
                return 'justica'
        else:
            return 'justica'

reclamacoes = float(input("Limite máximo de reclamações: "))
justica = float(input("Limite máximo de pedidos que vão para justiça: "))
adicionar = input("Quer adicionar mais dados? ")
pedidos = [[], [], []]
pedidos_relativos = [[], [], []]
total_pedidos = 0

if adicionar == 's' or adicionar == 'S':
    while True:
        if adicionar == 'S' or adicionar == 's':
            valor = float(input("Qual é o valor do pedido? "))
            atraso = int(input("Quantos dias em atraso? "))
            tamanho = input("Qual era o tamanho? ")
            avaria = input("Havia avaria no pedido? ")
            capital = input("A entrega foi para uma capital? ")
            classificacao = classifica_pedido(valor, atraso, tamanho, avaria, capital)
            
            if classificacao == 'reclamacao':
                pedidos[0].append(classificacao)
            elif classificacao == 'normal':
                pedidos[1].append(classificacao)
            else:
                pedidos[2].append(classificacao)
            
            total_pedidos += 1
            print(f"Pedido classificado como {classificacao}")
        else:
            break
        
        adicionar = input("Quer adicionar mais dados? ")
        
    for i in range(0, len(pedidos)):
        for j in range(len(pedidos[i])):
            if pedidos[i][j] == 'reclamacao':
                pedidos_relativos[0].append(100/total_pedidos)
            elif pedidos[i][j] == 'normal':
                pedidos_relativos[1].append(100/total_pedidos)
            elif pedidos[i][j] == 'justica':
                pedidos_relativos[2].append(100/total_pedidos)

    for i in range(len(pedidos_relativos)):
        pedidos_relativos[i] = sum(pedidos_relativos[i])

    print(f"Pedidos por classificação: {len(pedidos[0]):02d} reclamacao, {len(pedidos[1]):02d} normal, {len(pedidos[2]):02d} justica")
    print(f"Pedidos por classificação: {pedidos_relativos[0]:0>5.2f}% reclamacao, {pedidos_relativos[1]:0>5.2f}% normal, {pedidos_relativos[2]:0>5.2f}% justica")

    if pedidos_relativos[0] / 100 <= reclamacoes and pedidos_relativos[2] / 100 <= justica:
        print("Meta atingida!")
    else:
        print('Meta nao atingida!')
