def dias_do_ano(date: str) -> int:
    day, month, year = date.split('/')
    day, month, year = int(day), int(month), int(year)
    days = day - 1

    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    while month > 0:
        month -= 1
        for m, d in months.items():
            if month == m:
                days += d

    return days
