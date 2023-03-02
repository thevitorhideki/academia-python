def decodifica(encrypted: str, standards: list) -> str:
    standards = {y: x for x, y in standards.items()}
    decrypted = ''

    for i in encrypted:
        for k, v in standards.items():
            if i in standards:
                if i == k:
                    decrypted += v
            else:
                decrypted += i
                break

    return decrypted


print(decodifica('*b*c*t&', {'a': '*', 'e': '&'}))
