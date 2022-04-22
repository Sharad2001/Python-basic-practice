def multiplicationTable(N):
    for i in range(1, 11):
        print(i * N, end=" ")

def main():
    N = int(input())
    multiplicationTable(N)
    print()

if __name__ == '__main__':
    main()