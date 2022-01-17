# numbers = ["3", "34", "64"]
# numbers = list(map(int, numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# numbers[2] = numbers[2] + 1
# print(numbers[2])
# num = [2, 4, 5,67 ,45,453]
# square = list(map(lambda x: x*x, num))
# print(square)
# def square(a):
#     return a*a
#
# def cube(a):
#     return a**3
# func = [square, cube]
# for i in range(5):
#     val = list(map(lambda x: x(i), func))
#     print(val)

# Filter Function
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def is_greater_than_5(num):
#     return num>5
# gr_than_5 = list(filter(is_greater_than_5, list_1))
# print(gr_than_5)

# Reduce Function

from functools import reduce
list_1 = [1, 2, 3, 4]
num = reduce(lambda x,y : x+y, list_1)
# num = 0
# for i in list_1:
#     num = num+i
print(num)