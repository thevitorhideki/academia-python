def calcula_media(students):
    grade = 0
    number_of_students = 0

    for i in students:
        for j in i.values():
            grade += j
            number_of_students += 1

    return grade/number_of_students
