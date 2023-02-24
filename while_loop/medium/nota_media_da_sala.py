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

def nota_final(quiz, Ai, Af, EP1, EP2, Pf):
    nota_individual = 0.4 * Ai + 0.5 * Af + 0.1 * quiz
    nota_grupo = 0.1 * EP1 + 0.2 * EP2 + 0.7 * Pf
        
    if nota_individual >= 5 and nota_grupo >= 5:
        nota_final = (nota_individual + nota_grupo) / 2 
    elif nota_individual < 5 or nota_grupo < 5:
        nota_final = min(nota_individual, nota_grupo)

    return nota_final

sala = []
classificacao = [[], []]
adicionar = input("Deseja adicionar a nota de um aluno? ")

if adicionar == 'sim' and 'Sim':
    while True:
        if adicionar == 'sim' and 'Sim':
            quizzes = []
            for i in range(5):
                quizzes.append(float(input("Digite a nota dos quizzes: ")))
            Ai = float(input("Digite a nota da Ai: "))
            Af = float(input("Digite a nota da Af: "))
            EP1 = float(input("Digite a nota da EP1: "))
            EP2 = float(input("Digite a nota da EP2: "))
            Pf = float(input("Digite a nota do Pf: "))

            nota_quiz = nota_quizzes(quizzes)
            nota = nota_final(nota_quiz, Ai, Af, EP1, EP2, Pf)

            sala.append(nota)

            if nota >= 5:
                classificacao[0].append(nota)
            else:
                classificacao[1].append(nota)

            print(f"Nota final do aluno: {nota:.2f}")
            adicionar = input("Deseja adicionar a nota de um aluno? ")
        else:
            break
        
    media = sum(sala) / len(sala)
    print(f"Média da sala: {media:.2f}")

    aprovados = 100 * (len(classificacao[0]) / len(sala))
    reprovados = 100 * (len(classificacao[1]) / len(sala))
    print(f'Aprovados: {aprovados:.2f}%')
    print(f'Reprovados: {reprovados:.2f}%')
else:
    print("Média da sala: 0.00")
    print("Aprovados: 0.00%")
    print("Reprovados: 0.00%")
