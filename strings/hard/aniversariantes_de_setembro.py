def aniversariantes_de_setembro(birthdays: dict) -> dict:
    september_birthday = {k: v for k, v in birthdays.items() if v[4] == '9'}

    return september_birthday
