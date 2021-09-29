def EvenOdd(l):
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

l = []
n = int(input("Enter the number of element in a list: "))
for i in range(0, n):
    ele = int(input("Enter the element of list: "))
    l.append(ele)

even,odd = EvenOdd(l)
print(f"The list of even number will be {even}")
print(f"The list of odd number will be {odd}")