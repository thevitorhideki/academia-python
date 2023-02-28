import math

def reflexao_total_interna(n1, n2, teta2):
    teta1 = math.asin(math.radians((n2 * math.sin(math.radians(teta2))) / n1))
    limite = math.asin(math.radians(n1 / n2))
    
        if teta1 > limite:
        return True
    
    return False
