def greater_than_no(l, n):
    for i in l:
        if n < i:
            return False
    return True

l = []
n = int(input("Enter the number which you want to check: "))
m = int(input("Enter the number of elements in list: "))
for i in range(m):
    ele = int(input("Enter the element: "))
    l.append(ele)
if(greater_than_no(l, n)):
    print(f"Yessss!! All the elements in the list are greater than {n}.")
else:
    print(f"Sorry!! all the elements in list are not greater than {n}.")
