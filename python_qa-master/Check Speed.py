import math


def check_speed(speed):
    if speed <= 70:
        print('Ok!!')
    else:
        _check_speed = math.ceil((speed - 70) / 5)
        if _check_speed >= 12:
            print('License suspended')
        else:
            print('Point: ', _check_speed)


if __name__ == "__main__":
    while True:
        try:
            speed = int(input("Your speed is:"))
            break
        except ValueError:
            print('Error Param. Please try again!')
            continue
    check_speed(speed)

