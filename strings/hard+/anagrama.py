def anagrama(word1: str, word2: str) -> bool:
    word1, word2 = list(word1), list(word2)
    word1, word2 = sorted(word1), sorted(word2)
    if word1 == word2:
        return True
    return False
