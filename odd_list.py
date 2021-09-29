def getOdd(l):
    res = None
    for x in l:
        count = l.count(x)
        if count % 2 != 0:
            res = x
            break
    return res

l = []
n = int(input("Enter the number of element in list: "))
for i in range(n):
    ele = int(input("Enter the each element of list: "))
    l.append(ele)

print(f"Odd number of element will be {getOdd(l)}.")