def aniversariantes_de_setembro(birthdays: dict) -> dict:
    september_birthday = {}

    for k, v in birthdays.items():
        if v[4] == '9':
            september_birthday[k] = v

    return september_birthday
