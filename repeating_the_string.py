def combo_string(a, b):
    if len(a) > len(b):
        short = b
        longer = a
    elif len(a) < len(b):
        short = a
        longer = b
    return short + longer + short

def main():
    string = input().split()
    string1 = string[0]
    string2 = string[1]

    print(combo_string(string1, string2))

if __name__ == '__main__':
    main()