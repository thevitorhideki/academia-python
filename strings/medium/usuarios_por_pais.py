def usuarios_por_pais(emails: list, domains: dict) -> dict:
    users = {}

    for k, v in domains.items():
        for email in emails:
            if k in email:
                users.setdefault(v, []).append(email[:email.find('@')])

    return users
