def miniMaxSum(arr):
    a = sorted(arr)
    high = 0
    low = 0
    for i in range(0, 4):
        low = low+a[i]
    for j in range(1, 5):
        high = high + a[j]
    print(low, high)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)