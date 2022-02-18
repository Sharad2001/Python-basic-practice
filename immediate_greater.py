class Solution:

    def immediateGreater(self, arr, n, x):
        res = []
        for i in arr:
            if i > x:
                res.append(i)
        if len(res) == 0:
            return -1
        else:
            return min(res)

if __name__ == '__main__':

    n = int(input("Enter the length of array: "))
    arr = [int(e) for e in input("Enter the element of array: ").split()]
    x = int(input("Enter value of integer: "))

    ans = Solution().immediateGreater(arr, n, x)
    print(ans)