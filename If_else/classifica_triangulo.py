def classifica_triangulo(l1,l2,l3):
    if l1==l2 and l1==l3:
        return 'equilátero'
    elif l1 == l2 or l1 == l3 or l2 ==l3 :
        return 'isósceles'
    else:
        return 'escaleno'

print(classifica_triangulo(1,2,2))
print(classifica_triangulo(1,1,1))
print(classifica_triangulo(1,1,3))