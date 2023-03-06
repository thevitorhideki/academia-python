from datetime import datetime


def converteHora(time: str) -> str:
    d = datetime.strptime(time, '%H:%M')

    return d.strftime('%I:%M %p')
