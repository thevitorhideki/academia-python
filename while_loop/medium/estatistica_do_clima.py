dias = int(input("Quantos dias quer analisar? "))
choveu = 0
fez_frio = 0
usou_guarda_chuva = 0
usou_casaco = 0

n = 1
while n <= dias:
    chuva = input("Choveu? ")
    if chuva == 's' or chuva == 'S':
        choveu += 1
    
    temp_min = float(input("Temperatura mínima: ")) 
    if temp_min < 20:
        fez_frio += 1
    
    guarda_chuva = input("Tinha guarda-chuva? ")
    if guarda_chuva == 's' or guarda_chuva == 'S':
        if chuva == 's' or chuva == 'S':
            usou_guarda_chuva += 1
            
    casaco = input("Usou casaco? ")
    if casaco == 's' or casaco == 'S':
        if temp_min < 20:
            usou_casaco += 1

    n += 1

print(f"Choveu em {choveu} de {dias} dias")
print(f"Fez frio em {fez_frio} de {dias} dias")
print(f"Usou guarda-chuva em {usou_guarda_chuva} de {choveu} dias de chuva")
print(f"Usou casaco em {usou_casaco} de {fez_frio} dias de frio")
