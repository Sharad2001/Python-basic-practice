def logical(a, b):
    print(a and b)
    print(a or b)
    print(not a)

def main():
    testcases = int(input())
    while (testcases > 0):
        a = int(input())
        b = int(input())
        logical(a, b)
        testcases -= 1

if __name__ == '__main__':
    main()