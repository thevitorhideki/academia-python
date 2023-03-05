def valida_senha(password):
    special_characters = ['?', '!', '@', '#', '$', '%', '&', '*']
    count_special = 0

    if len(password) < 8 and any(password[i] == password[i+1] for i in range(len(password) - 1)):
        return False

    for i in special_characters:
        if i in password:
            count_special += 1

    if count_special >= 2:
        return True

    return False
