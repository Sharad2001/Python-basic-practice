def join_middle(bound_by, tag_name):
    return bound_by[0:len(bound_by) // 2] + tag_name + bound_by[len(bound_by) // 2:]

def main():
    string = input().split()
    bound_by = string[0]
    tag_name = string[1]

    print(join_middle(bound_by, tag_name))

if __name__ == '__main__':
    main()