def show_star(n):
    star = ""
    for item in range(n):
        star += '*'
        print(star)


if __name__ == '__main__':
    n = int(input("Please input n: "))
    show_star(n)