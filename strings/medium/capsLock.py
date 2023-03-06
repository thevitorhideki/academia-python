def capsLock(text: str) -> str:
    fixed = ''
    for i in text:
        if i.upper() == i:
            fixed += i.lower()
        else:
            fixed += i.upper()

    return fixed
