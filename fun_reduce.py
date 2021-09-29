from functools import reduce

list1 = [2, 4, 7, 9, 1, 3]
sum_of_list1 = reduce(lambda x, y: x + y, list1)

list2 = ["abc", "xyz", "def"]
max_of_list2 = reduce(lambda x, y: x if x>y else y, list2)

print("Sum of list1", sum_of_list1)
print("Maximum of list 2", max_of_list2)