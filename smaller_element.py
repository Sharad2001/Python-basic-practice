def getSmaller(l,x):
    res = []
    for i in l:
        if i < x:
            res.append(i)
    return res

l = []
n = int(input("Enter the number of element in a list: "))

for i in range(0, n):
    ele = int(input("Enter the element in a list: "))
    l.append(ele)

x = int(input("Enter the number below which you want to get a number in a list: "))
res = getSmaller(l,x)
print(f"The required list will be {res}")