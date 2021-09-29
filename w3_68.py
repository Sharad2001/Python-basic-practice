def getSum(n):
    sum = 0
    for i in str(n):
        sum = sum + int(i)

    return sum

n = int(input("Enter the number: "))
print(f"Sum of integer will {getSum(n)}")