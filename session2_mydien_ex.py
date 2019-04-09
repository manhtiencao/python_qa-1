import math

tt = "Y"
while tt.upper() == "Y":
    tt = input("Do you want to see exercise (Y) or exit (enter any key)? ")
    if tt.upper() == "Y":
        ex = -1
        while ex not in (1, 2, 3, 4):
            ex = input("\nWhich exercise would you like to see?? (1/2/3/4): ")
            ex = int(ex)

        # Write a function called fizz_buzz that takes a number.
        # If the number is divisible by 3, print “Fizz”.
        # If it is divisible by 5, it should return “Buzz”.
        # If it is divisible by both 3 and 5, it should return “FizzBuzz”.
        # Otherwise, print “Opps”
            if ex == 1:
                cont = "Y"
                while cont.upper() == "Y":
                    x = input("Please input x: ")
                    x = int(x)
                    while x < 0:
                        x = input("Please input x: ")
                        x = int(x)
                    cont = 0
                    if x % 3 == 0 and x % 5 == 0:
                        print("FizzBuzz")
                    elif x % 3 == 0:
                        print("Fizz")
                    elif x % 5 == 0:
                        print("Buzz")
                    else:
                        print("Opps")
                    cont = ""
                    while cont.upper() != "Y" and cont.upper() != "N":
                        cont = input("\nDo you want to continue? (Y/N): ")

                # Write a function called show_stars(rows). If rows is 5, it should print the following:
                # *
                # **
                # ***
                # ****
                # *****
            elif ex == 2:
                cont = "Y"
                while cont.upper() == "Y":
                    x = input("Please input x: ")
                    x = int(x) + 1
                    for i in range(0, x):
                        for j in range(0, i):
                            print("*", end='')
                        print("\n")
                    cont = ""
                    while cont.upper() != "Y" and cont.upper() != "N":
                        cont = input("\nDo you want to continue? (Y/N): ")

            # Write a function called showNumbers that takes a parameter called limit.
            # It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
            # For example, if the limit is 3, it should print:
            # 0 EVEN
            # 1 ODD
            # 2 EVEN
            # 3 ODD
            elif ex == 3:
                cont = "Y"
                while cont.upper() == "Y":
                    x = input("Please input x: ")
                    x = int(x)
                    i = 0
                    while i <= x:
                        if i % 2 == 0:
                            print(i, " EVEN")
                        else:
                            print(i, " ODD")
                        i = i + 1
                    cont = ""
                    while cont.upper() != "Y" and cont.upper() != "N":
                        cont = input("\nDo you want to continue? (Y/N): ")

            #  Write a program for checking the speed of drivers. This function should have one parameter: speed.
            # If speed is less than 70, it should print “Ok”.
            # Otherwise, for every 5km above the speed limit (70),
            # it should give the driver one demerit point and print the total
            # number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
            # If the driver gets more than 12 points, the function should print: “License suspended”
            elif ex == 4:
                cont = "Y"
                while cont.upper() == "Y":
                    speed = -1
                    while speed < 0:
                        speed = input("Please input speed (>0): ")
                        speed = int(speed)

                    if speed <= 70:
                        print("OK")
                    else:
                        point = 0
                        x = (speed - 70) / 5
                        # print("x = ", x)
                        x = math.ceil((speed - 70) / 5)
                        # print("x = ", x)
                        point = point + x
                        if point <= 12:
                            print("----Points: ", point)
                        else:
                            print("----Points: ", point)
                            print("----License suspended")
                    cont = ""
                    while cont.upper() != "Y" and cont.upper() != "N":
                        cont = input("\nDo you want to continue? (Y/N): ")
            else:
                break

