def extrai_nomes_de_usuarios(emails: list):
    names = [email[0:email.find('@')] for email in emails]

    return names
