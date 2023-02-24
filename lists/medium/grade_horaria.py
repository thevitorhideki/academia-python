def compromisso_no_periodo(grade, dia, periodo):
    if grade[periodo][dia] == '':
        return 'Livre'
    else:
        return grade[periodo][dia]
