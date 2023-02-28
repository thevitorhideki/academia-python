import math
def reflexao_total_interna (n1, n2, teta2):
    limite = math.asin(n1/n2)
    if math.radians(teta2) > limite:
        return True
    else:
        return False
