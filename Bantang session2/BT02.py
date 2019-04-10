while True:
    try:
        n = int(input("Pls input your number:"))
        if n>0:
            for x in range(0, n + 1):
                print('*' * x)
            break
        print(" pleas input interger")
    except Exception:
        print("Your number is incorrect\n")
    continue
print("Thanks for your review and comment!")