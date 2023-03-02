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
