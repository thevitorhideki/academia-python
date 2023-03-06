def pos_arroba(word: str) -> int:
    for i in range(len(word)):
        if word[i] == '@':
            return i
