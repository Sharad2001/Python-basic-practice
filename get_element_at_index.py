def getByIndex(arr, n, idx):
    if idx >= n:
        return -1
    else:
        return arr[idx]

if __name__ == '__main__':
    # tcs = int(input("Enter a number: "))
    #
    # for _ in range(tcs):
    n = int(input("Enter the no. of elements in array: "))
    arr = [int(x) for x in input("Enter the elements: ").split()]

    idx = int(input("Enter the index value: "))

    print(getByIndex(arr, n, idx))
