def fizz_buzz(n):
    if n % 3 == 0 & n % 5 == 0:
        print ("Fizz & Buzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print ("Buzz")
    else:
        print("Opps")


def show_star(n):
        for x in range(1, n+1):
            print(x*"*")


def show_number(n):
    for x in range(n):
        if x % 2 == 0:
            print(x, "EVEN")
        else:
            print(x, "ODD")


def check_speed(speed):
    if speed <= 70:
        print("Ok")
    else:
        point = (speed - 70)//5
        print("The spped is ", speed, "point is", point)
        if point > 12:
            print('License suspended')


if __name__ == '__main__':
    n = int(input("input n:"))
    while True:
        if n >= 0:
            break
        print ('Number is invalid')
        n = int(input("Input again n:"))
    print("---------Bai 1 --------")
    fizz_buzz(n)
    print("---------Bai 2 --------")
    show_star(n)
    print("---------Bai 3 --------")
    show_number(n)
