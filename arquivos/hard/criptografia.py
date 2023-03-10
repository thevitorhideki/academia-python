with open('hard/criptografado.txt', 'r') as file:
    content = file.read()
    content = content.split('\n')

    keys = {'s': 'z', 'a': 'e', 'r': 'b', 'b': 'r', 'e': 'a', 'z': 's'}

    for phrase in content:
        dec_phrase = ''
        for letter in phrase:
            if letter in keys:
                dec_phrase += keys[letter]
            else:
                dec_phrase += letter
        print(dec_phrase)
