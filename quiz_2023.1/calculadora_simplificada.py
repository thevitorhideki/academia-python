num = int(input("Insira o número: "))
op = input("Insira o operador: ")
final = num

while op != "=":
    if op != "+" and op != "-" and op != "*" and op != "/":
        print("Deveria ser um dos seguintes operadores: + - / * ou o =")
        op = input("Insira o operador: ")
    else:
        num = int(input("Insira o número: "))
        if op == "+":
            final += num
        elif op == "-":
            final -= num
        elif op == "*":
            final *= num
        elif op == "/":
            final /= num
        op = input("Insira o operador: ")

print(final)