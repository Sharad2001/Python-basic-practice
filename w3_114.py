nums = [34, 6, -39, 34, 0, -394]
print("Original number in list: ", nums)
new_nums = list(filter(lambda x: x>0, nums))
print("\nPositive number in the said list:", new_nums)
