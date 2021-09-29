import math
def hypotenuse(p, b):
    h = math.sqrt(p**2 + b**2)
    return h

p = int(input("Enter the perpendicular height of the triangle: "))
b = int(input("Enter the base of triangle: "))
print(f"Hypotenuse of the triangle will be: {hypotenuse(p, b)}")