def concatenate_N(list1):
    list2 = "-".join(list1)
    return list2

list1 = []
n = int(input("Enter the number of items you wanted to concatenate: "))
for i in range(n):
    ele = input()
    list1.append(ele)
print(concatenate_N(list1))