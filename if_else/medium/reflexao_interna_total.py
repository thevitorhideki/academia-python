import math

def reflexao_total_interna(n1, n2, teta2):
    teta1 = math.asin(math.sin(math.radians(teta2)) * n2 / n1)
    if teta1 > 90:
        return True
    else:
        return False