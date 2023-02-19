import math 

def snell_descartes(n1, n2, angulo1):
    angulo2 = (n1 * math.sin(math.radians(angulo1))) / n2
    
    return math.degrees(angulo2)
