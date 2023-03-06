import re

pattern = '[A,E,I,O,U]'
while True:
    word = input("Digite uma palavra: ")
    if word == 'fim':
        print('Até a próxima')
        break
    print(re.sub(pattern, '', word, flags=re.IGNORECASE))
