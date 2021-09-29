def sum(a, b):
    if 15< a + b <=20:
        sum = 20
    else:
        sum = a + b

    return sum

a = int(input("Enter the first integer: "))
b = int(input("Enter thr second integer: "))

print(f"sum = {sum(a, b)}")