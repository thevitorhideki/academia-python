def esconde_senha(password: str) -> str:
    password_hide = ''
    for i in range(len(password)):
        password_hide += '*'

    return password_hide
