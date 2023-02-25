def traduz(eng_words: list, eng2port: dict) -> list:
    translated = []

    for i in eng_words:
        for k, v in eng2port.items():
            if i == k:
                translated.append(v)

    return translated
