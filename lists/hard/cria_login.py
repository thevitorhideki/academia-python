def login_disponivel(login: str, existent_logins: list):
    same_login = [i for i in existent_logins if login in i]

    if login not in existent_logins:
        return login
    login += str(len(same_login))

    return login


logins = []

while True:
    login = input('Digite um login: ')

    if login == 'fim':
        break
    else:
        logins.append(login_disponivel(login, logins))

for i in logins:
    print(i)
