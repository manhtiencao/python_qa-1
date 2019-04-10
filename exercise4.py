# 4. Write a program for checking the speed of drivers. This function should
# have one parameter: speed.
#  If speed is less than 70, it should print “Ok”.
#  Otherwise, for every 5km above the speed limit (70), it should give the
# driver one demerit point and print the total number of demerit points. For
# example, if the speed is 80, it should print: “Points: 2”.
#
#  If the driver gets more than 12 points, the function should print: “License
# suspended”

OK = float(70)
speed = float(input("Nhập vào tốc độ (km/h): "))
if speed <= OK:
    print("Ok")

else:
    points = int((speed - OK) / 5)
    if points <= 12:
        print("Points:", points)
    else:
        print("License suspended")
