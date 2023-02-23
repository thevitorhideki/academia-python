import math

def reflexao_total_interna(n1, n2, teta2):
    if teta2<0:
        teta2=-1*teta2   
        teta2=math.radians(teta2)
        if teta2>=math.pi/2:
            return False
        else:
            teta1 = math.asin(n2 * math.sin(teta2) / n1)
            if math.sin(teta1) > 1:
                return True
            else:
                return False
    else:
        teta2=math.radians(teta2)
        teta1 = math.asin(n2 * math.sin(teta2) / n1)
        if math.sin(teta1) > 1:
            return True
        else:
            return False

print(reflexao_total_interna(1,2,-90))