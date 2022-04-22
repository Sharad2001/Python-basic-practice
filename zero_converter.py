def pos(n):
    if n == 0:
        print("already zero")
    while n > 0:
        print(n - 1, end=" ")
        n = n - 1

def neg(n):
    while n <= 0:
        print(n, end=" ")
        n += 1

def main():
    n = int(input())
    if (n > 0):
        pos(n)
    elif (n < 0):
        neg(n)
    else:
        print("already Zero", end="")
    print()

if __name__ == '__main__':
    main()