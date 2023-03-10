import math


class Circulo():
    def __init__(self, center, r) -> None:
        self.center = center
        self.r = r

    def contem(self, ponto):
        distance = math.sqrt((ponto.x - self.center.x)
                             ** 2 + (ponto.y - self.center.y) ** 2)

        if distance > self.r:
            return False

        return True
