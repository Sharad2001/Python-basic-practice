from functools import reduce

nums = [10, 20, 30]
print("Original list numbers: ")
print(nums)
num_products = reduce((lambda a, b: a*b), nums)
print("\nProduct of integer of list will be:", num_products)