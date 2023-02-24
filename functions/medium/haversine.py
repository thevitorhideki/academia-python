import math

def haversine(raio, latitude1, longitude1, latitude2, longitude2):    
    distance = 2 * raio * math.asin(math.sqrt(math.sin(math.radians((latitude2 - latitude1) / 2)) ** 2 + math.cos(math.radians(latitude1)) * math.cos(math.radians(latitude2)) * math.sin(math.radians((longitude2 - longitude1) / 2)) ** 2))
    
    return distance

