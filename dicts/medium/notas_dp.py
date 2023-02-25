def notas_dp(grades: list[dict]):
    dp = []
    mean = 0

    for students in grades:
        for grade in students.values():
            if grade <= 10:
                mean += grade
        if mean / 2 < 5:
            dp.append(students['matricula'])

        mean = 0

    return dp
