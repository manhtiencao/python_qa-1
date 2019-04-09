import math


def check_speed(speed):
    if speed <= 70:
        print("Ok")
    else:
        point = int(math.ceil((speed - 70) / 5.0))
        print("The spped is ", speed, "point is", math.ceil(point))
        if point > 12:
            print('License suspended')


if __name__ == '__main__':
    speed = int(input("input speed:"))
    check_speed(speed)
