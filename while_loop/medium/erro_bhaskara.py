import math

x = 0
diferenca = []
while x <= 90:
    bhaskara = math.asin(math.radians((4 * x * (180 - x)) / (40500 - x * (180 - x))))
    math_sin = math.sin(math.radians(x))
    diferenca.append(abs(bhaskara - math_sin))
    x += 1

print(max(diferenca))

