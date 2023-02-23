classificacao=input()
vermelhos=int(input())
laranjas=int(input())
azuis=int(input())

if classificacao=="V":
    tempo=vermelhos*7
    print(tempo)
elif classificacao=="L":
    tempo=vermelhos*7+laranjas*5
    print(tempo)
elif classificacao=="A":
    tempo=vermelhos*7+laranjas*5+azuis*5
    print(tempo)
