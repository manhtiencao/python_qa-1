def show_number(n):
    for x in range(0, n + 1):
        if x % 2 == 0:
            print(x, "Even")
        else:
            print(x, "ODD")


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Input number:"))
            if n > 0:
                show_number(n)
                break
            print("Please Try Again")
            print("-"*30)
        except Exception as err:
            print("Error:", err)
        continue
