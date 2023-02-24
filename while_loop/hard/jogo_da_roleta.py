from random import randint

money = 100
while money > 0:
    print(f"Dinheiro disponível: {money}")

    valor_aposta = float(input("Aposte um valor: "))
    if valor_aposta != 0:
        aposta = input("Qual aposta? ")

        if aposta == 'n':
            numero = int(input("Digite um número de 1 a 36: "))
            if randint(0, 36) == numero:
                valor_aposta *= 35
                money += valor_aposta
            else:
                money -= valor_aposta
        elif aposta == 'p':
            par_impar = input("Par ou ímpar? ")
            if par_impar == 'p':
                if randint(0, 36) % 2 == 0:
                    money += valor_aposta
                else:
                    money -= valor_aposta
            elif par_impar == 'i':
                if randint(0, 36) % 2 != 0:
                    money += valor_aposta
                else:
                    money -= valor_aposta
    else:
        break
