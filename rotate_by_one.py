def rotateByOne(l):
    n = len(l)
    x = l[0]
    for i in range(1,n):
        l[i-1] = l[i]
    l[n-1] = x

l = []
m = int(input("Enter the number of element of list: "))
for i in range(m):
    ele = int(input("Enter the each element of list: "))
    l.append(ele)

print(f"Original list is: {l}")
rotateByOne(l)
print(f"Rotated list is: {l}")