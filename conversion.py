def print_formatted(number):
    
    l = len(bin(n)) - 2
    for i in range(1, n+1):
        f = ""
        for c in "doXb":
            if f:
                f += " "
            f += "{:>"+str(l) + c + "}"
        print(f.format(i, i, i, i))

if __name__ == '__main__':
    n = int(input("Enter the number: "))
    print_formatted(n)