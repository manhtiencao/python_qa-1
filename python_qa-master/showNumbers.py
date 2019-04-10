def show_number(n):
    for x in range(0, n + 1):
        if x % 2 == 0:
            print(x, "Even")
        else:
            print(x, "ODD")


if __name__ == "__main__":
    try:
        n = int(input("Input number:"))
        show_number(n)
    except Exception as err:
        print('error=%s', err)
