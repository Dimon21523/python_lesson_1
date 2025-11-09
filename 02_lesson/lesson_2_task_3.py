import math

def square(side):
    area = side * side 
    return math.ceil(area)

side = 4.3
result = square(side)
print(f"Площадь квадрата со стороной {side} равна {result}")