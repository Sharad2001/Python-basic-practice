def average(l,n):
    sum = 0
    for i in l:
        sum = sum+i


    return sum/n

l = []
n = int(input("Enter the length of list: "))
for i in range(0, n):
    ele = int(input("Enter the element: "))

    l.append(ele)
print("Average of list will be: ")
print(average(l,n))