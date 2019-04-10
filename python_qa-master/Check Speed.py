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
            if speed > 0:
                check_speed(speed)
                break
            print("Please Try again")
            print("-"*30)
        except Exception as err:
            print("Error:", err)
            print("Try again!!")
            print("-"*30)
            continue

