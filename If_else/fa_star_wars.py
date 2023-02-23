cont_sim=0

pergunta1=input('Já assistiu todos os filmes? ')
if pergunta1 == 'sim':
    cont_sim+=1
pergunta2=input('Tem camiseta temática? ')
if pergunta2 == 'sim':
    cont_sim+=1
pergunta3=input('Já se fantasiou de algum personagem? ')
if pergunta3 == 'sim':
    cont_sim+=1
pergunta4=input('Tem algum action figure/nave/etc?')
if pergunta4 == 'sim':
    cont_sim+=1
pergunta5=input('Já foi no Galaxy\'s Edge, o parque temático da franquia?')
if pergunta5 == 'sim':
    cont_sim+=1

if cont_sim>=5:
    print('One with the Force')
elif cont_sim>=3 and cont_sim<=4:
    print('Jedi')
elif cont_sim>=2 and cont_sim<3:
    print('Padawan')
else:
    print('Inocente')
