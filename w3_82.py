def sum_of_list(l, n):
    sum = 0
    for i in range(n):
        sum = sum+ l[i]
    return sum
l = []
n = int(input("Enter the number of elements in list: "))
for i in range(n):
    ele = int(input("Enter the element: "))
    l.append(ele)
print(sum_of_list(l,n))