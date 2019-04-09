speed = int(input("Speed of drivers: "))

if (speed <= 70):
    print("Speed Ok")
else:
    kq = speed - 70
    point = kq/5
    point2 = kq%5
    if point2 > 0:
        print("Point: ", int(point + 1))
    else:
        print("Point: " , int(point))
        if point >= 12:
            print("License suspended")

