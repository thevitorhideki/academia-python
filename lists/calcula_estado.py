def nota_quizzes(quiz):
    minimo = min(quiz[0], quiz[1], quiz[2], quiz[3], quiz[4])

    if minimo == quiz[0]:
        return (quiz[1] + quiz[2] + quiz[3] + quiz[4]) / 4
    elif minimo == quiz[1]:
        return (quiz[0] + quiz[2] + quiz[3] + quiz[4]) / 4
    elif minimo == quiz[2]:
        return (quiz[0] + quiz[1] + quiz[3] + quiz[4]) / 4
    elif minimo == quiz[3]:
        return (quiz[0] + quiz[1] + quiz[2] + quiz[4]) / 4

    return (quiz[0] + quiz[1] + quiz[2] + quiz[3]) / 4


def calcula_estado(students):
    students_grades = []
    for i in students:
        quiz = nota_quizzes(i[1])
        AI = i[2][0]
        AF = i[2][1]

        if quiz * 0.1 + AI * 0.4 + AF * 0.5 >= 5:
            students_grades.append([i[0], 'A'])
        else:
            students_grades.append([i[0], 'R'])
    return students_grades
