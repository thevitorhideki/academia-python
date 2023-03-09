import re


def valida_exp(expression: str) -> bool:
    replacements = {
        '[=]': ' = ',
        '[+]': ' + ',
        '[-]': ' - ',
        '[*]': ' * ',
        '[/]': ' / '
    }

    # Colocar espaço entre os números e os operadores
    for key, value in replacements.items():
        expression = re.sub(key, value, expression)

    expression = expression.split()

    # Troca os números romanos por números
    for i in range(len(expression)):
        if 'I' in expression[i]:
            expression[i] = str(len(expression[i]))

    # Executa a expressão da esquerda para a direita ignorando a ordem dos operadores
    result = expression[0]
    for i in expression[1:-2]:
        if i.isalnum():
            result += i
            result = str(eval(result))
        else:
            result += i

    equals = expression[-1]

    return result == equals
