import math
def will_it_float(P,R,r):
    P=1000*P
    volume=2*(math.pi**2)*R*(r**2)
    densidade=P/volume
    if densidade<=0.997:
        return True
    else:
        return False

print(will_it_float(16,24,6))