def updateArray(arr, n, idx, element):
    # code here
    if n > idx:
        arr.insert(idx, element)

if __name__ == '__main__':

    n = int(input("Size of array: "))
    idx, element = [int(x) for x in input("Enter the index value and element: ").split()]

    arr = [i + 1 for i in range(n)]

    updateArray(arr, n, idx, element)

    print(f"The {idx} position of array becames: {arr[idx]}")
