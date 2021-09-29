x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))
z = int(input("Enter the third integer: "))
a1 = max(x, y, z)
a3 = min(x, y, z)
a2 = (x+y+z) - (a1+a3)

print(a1, a2, a3)