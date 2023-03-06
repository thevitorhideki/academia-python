from datetime import datetime


def calcula_idade(birthday: str, date: str) -> int:
    bday = datetime.strptime(birthday, "%d/%m/%Y")
    today = datetime.strptime(date, "%d/%m/%Y")
    age = today.year - bday.year - \
        ((today.month, today.day) < (bday.month, bday.day))

    return age
