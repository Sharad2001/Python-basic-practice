def getReverse(l):
    s = 0
    e = len(l) - 1
    while s < e:
        l[s], l[e] = l[e], l[s]
        s = s+1
        e = e - 1

l = []
n = int(input("Enter the number of element of list: "))
for i in range(n):
    ele = int(input("Input each element: "))
    l.append(ele)
getReverse(l)
print(f"Reverse list is {l}")