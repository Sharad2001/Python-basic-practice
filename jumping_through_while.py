def printIncreasingPower(x):
    i = 1
    while (i ** 2 <= x):
        print(i ** 2, end=" ")
        i = i + 1

def main():
    x = int(input())
    printIncreasingPower(x);
    print()
if __name__ == '__main__':
    main()