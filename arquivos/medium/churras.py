import re


with open('churras.txt', 'r') as file:
    content = file.readlines()
    content = re.sub('[\n]', '', content)
    print(content)
