while True:
    try:
        n = int(input("Pls input your number:\n "))
        if n>0:
            if n<70:
                print("OK")
            else:
                if (n-70)%5 ==0:
                    point = (n-70)//5
                    if point >=12:
                        print("License suspended")
                    else:
                        print("Your point:", point +1)
                else:
                    point = (n-70)//5 +1
                    if point >=12:
                        print("License suspended")
                    else:
                        print("Your point:", point +1)
            break
        print("Pls inter interger!\n")
    except Exception:
        print(" Your number is incorrect format!")
    continue
print("Thanks for your review and comment!")