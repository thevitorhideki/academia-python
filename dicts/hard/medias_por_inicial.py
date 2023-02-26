def medias_por_inicial(students: dict) -> dict:
    mean_by_initial = {}

    for k, v in students.items():
        mean_by_initial.setdefault(k[0], []).append(v)

    for letter, grades in mean_by_initial.items():
        mean_by_initial[letter] = sum(grades) / len(grades)

    return mean_by_initial
