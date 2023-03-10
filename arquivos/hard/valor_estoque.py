import json

with open('estoque.json', 'r') as jsonfile:
    content = jsonfile.read()

storage = json.loads(content)

total = 0
for products in storage['produtos']:
    total += products['quantidade'] * products['valor']

print(total)
