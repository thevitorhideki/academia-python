words = []

while True:
    word = input('Digite uma palavra: ')
    if word == 'fim':
        break
    words.append(word)

for word in words:
    if word[0] == 'a':
        print(word)
