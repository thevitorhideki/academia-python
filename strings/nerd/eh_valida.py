def eh_valida(expression: str) -> bool:
    stack = []
    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            open_char = stack.pop()
            if (open_char == '(' and char != ')') or \
               (open_char == '[' and char != ']') or \
               (open_char == '{' and char != '}'):
                return False

    return not stack
