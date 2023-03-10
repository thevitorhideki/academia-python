with open('texto.txt', 'r') as file:
    content = file.read()
    content = content.split()

    print(len(content))
