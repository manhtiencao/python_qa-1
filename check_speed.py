def check_speed(speed):
    if speed <= 70:
        print("Ok")
    else:
        point = (speed - 70)//5
        print("The spped is ", speed, "point is", point)
        if point > 12:
            print('License suspended')


if __name__ == '__main__':
    speed = int(input("input speed:"))
    check_speed(speed)
