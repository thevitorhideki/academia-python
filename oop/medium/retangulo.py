class Retangulo:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def calcula_perimetro(self):
        self.x_side = (self.point_2.x - self.point_1.x)
        self.y_side = (self.point_2.y - self.point_1.y)

        return (self.x_side * 2) + (self.y_side * 2)

    def calcula_area(self):
        return self.x_side * self.y_side
