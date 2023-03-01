import re


def verifica_ganhador(words: str, players: dict) -> dict:
    count = {x: 0 for x in players.keys()}
    clean_words = re.sub(r'[^\w\s]', '', words)

    for player, player_word in players.items():
        for i in range(len(player_word)):
            for word in clean_words.lower().split():
                if word == player_word[i]:
                    count[player] += 1

    return count


print(verifica_ganhador('Algum tempo hesitei se devia abrir estas memórias pelo princípio ou pelo fim, isto é, se poria em primeiro lugar o meu nascimento ou a minha morte. Suposto o uso vulgar seja começar pelo nascimento, duas considerações me levaram a adotar diferente método: a primeira é que eu não sou propriamente um autor defunto, mas um defunto autor, para quem a campa foi outro berço; a segunda é que o escrito ficaria assim mais galante e mais novo. Moysés, que tambem contou a sua morte, não a poz no introito, mas no cabo: diferença radical entre este livro e o Pentateuco.',
      {
          'joao': ['paz', 'memórias', 'fim'],
          'maria': ['defunto', 'livro', 'felicidade']
      }))
