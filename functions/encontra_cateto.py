import math

def encontra_cateto(cateto1, hipotenusa):
    cateto2 = math.sqrt(hipotenusa**2 - cateto1**2)
    
    return cateto2
