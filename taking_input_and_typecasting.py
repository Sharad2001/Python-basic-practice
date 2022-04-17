def inPut():
    a = int(input())  ## a is integer
    b = str(input())  ## b is string
    c = float(input())  ## c is float
    d = bool(input())  ## d is a boolean

    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))

def main():
    testcases = int(input())
    while (testcases > 0):
        inPut()
        testcases -= 1

if __name__ == '__main__':
    main()