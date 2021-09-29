def sum(a, b, c):
    if a == b or b == c or a == c:
        sum = 0

    else:
        sum = a + b + c

    return sum

a = int(input("Enter the first integer "))
b = int(input("Enter the second integer "))
c = int(input("Enter the third integer "))

print(f"sum = {sum(a, b, c)}")