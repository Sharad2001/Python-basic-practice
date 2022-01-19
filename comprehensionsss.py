# --------------List Comprehension---------------
ls = [i for i in range(100) if i % 3== 0]
print(ls)

# -------------Dictionary Comprehension-------------
dict1 = {i:f"item {i}" for i in range(5)}
dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n", dict2)

# -----------Set Comprehension------------------
dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress2", "dress1", "dress2"]}
print(dresses)

# ----------Generator Comprehension--------------
evens = (i for i in range(10) if i%2==0)
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())