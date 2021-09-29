def sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

n = int(input("Enter upto which number you want sum: "))
print(f"Sum of first {n} natural number will be {sum(n)}")