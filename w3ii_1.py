def getDistinct(n):
    if len(n) == len(set(n)):
        return True
    else:
        return False

n = input("Enter the number: ")
print(getDistinct(n))