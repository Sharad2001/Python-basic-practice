import textwrap

def wrap(string, max_width):
    l1 = textwrap.wrap(string, width= max_width)
    l2 = '\n'.join(map(str,l1))
    return l2
if __name__ == '__main__':
    string, max_width = input("Enter the text: "), int(input("Enter the digit: "))
    result = wrap(string, max_width)
    print(result)