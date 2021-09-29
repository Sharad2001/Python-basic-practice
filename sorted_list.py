def getSorted(l):
    i = 1
    while i < len(l):
        if l[i] < l[i-1]:
            return False
            i = i+1
    return True

l = []
n = int(input("Enter the number of element in list: "))
for i in range(0, n):
    ele = int(input())
    l.append(ele)

if getSorted(l):
    print("Yes")

else:
    print("No")