# 1.Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, print Fizz.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, print “Opps”


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print("Opps")


# 2.Write a function called show_stars(rows). If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****

def show_stars(rows):
    i = 1
    while (i <= rows):
        print("*" * i)
        i += 1


# 3.Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

def showNumbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            print(i, " EVEN")
        else:
            print(i, " ODD")


# 4. Write a program for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”

def checkSpeed(speed):
    if speed < 70:
        print("Ok")
    else:
        point = 1 + (speed - 70) // 5
        if point <= 12:
            print("Point: ", point)
        else:
            print("License suspended")


# Test
fizz_buzz(30)
show_stars(5)
showNumbers(7)
checkSpeed(560)