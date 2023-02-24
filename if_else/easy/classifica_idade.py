def classifica_idade(idade):
    if idade>=18:
        return 'adulto'
    else:
        if idade >= 12 and idade <= 17:
            return 'adolescente'
        else:
            return 'crianca'

print(classifica_idade(11))
print(classifica_idade(17))
print(classifica_idade(21))