class Solution:
    # Function to find element with more appearances between two elements in an array.
    def majorityWins(self, arr, n, x, y):
        # code here
        res_x = []
        res_y = []
        for i in arr:
            if i == x:
                res_x.append(i)
            elif i == y:
                res_y.append(i)
        if len(res_x) > len(res_y):
            return x
        elif len(res_y) > len(res_x):
            return y
        elif len(res_x) == len(res_y):
            return min(x, y)

if __name__ == '__main__':

    n = int(input("Enter length of array: "))
    arr = [int(x) for x in input("Enter the elements of array: ").strip().split()]

    x, y = map(int, input("Enter value of x and y: ").strip().split())

    print(Solution().majorityWins(arr, n, x, y))
