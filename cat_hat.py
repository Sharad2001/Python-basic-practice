def cat_hat(str):
    n_cat = str.count("cat")
    n_hat = str.count("hat")
    return n_cat == n_hat

def main():
    str = input()
    print(cat_hat(str))


if __name__ == '__main__':
    main()