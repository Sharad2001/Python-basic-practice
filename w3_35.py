def test_number(a,b):
    if a == b or (a+b) == 5 or abs(a-b) == 5:
        return True

    else:
        return False

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(test_number(a,b))