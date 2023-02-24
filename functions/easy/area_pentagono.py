import math

def area_pentagono(lado):
    apotema = lado / (2 * math.tan(math.pi / 5))
    pentagono = apotema * lado * 5/2
    
    return pentagono

