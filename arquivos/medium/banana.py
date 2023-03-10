with open('macacos-me-mordam.txt', 'r') as file:
    content = file.read()
    content = content.lower().split()
    count = 0
    for i in content:
        if i == 'banana':
            count += 1

    print(count)
