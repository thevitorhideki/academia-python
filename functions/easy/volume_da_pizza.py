import math 

def volume_da_pizza(raio, altura):
    area_base = math.pi * (raio**2)
    volume = area_base * altura
    
    return volume
