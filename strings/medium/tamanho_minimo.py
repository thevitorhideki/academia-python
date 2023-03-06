def tamanho_minimo(word: str, length: int) -> list:
    valid_passwords = []
    words = word.split(' ')

    for i in words:
        if len(i) >= length:
            valid_passwords.append(i)
    return valid_passwords
