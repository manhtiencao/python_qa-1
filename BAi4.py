import math
def speed(n):
    limit = 70
    if n < 70:
        print("OK")
    else:
        point = math.ceil((n - limit) / 5)
        if point >= 12:
            print("License suspended")
        else:
            print("Points: ", point)

toc_do = 0
while (toc_do <= 0):
    try:
        toc_do = int(input('Nhap vao toc do  '))
    except ValueError:
        print("No.. input string is not a number. It's a string")
speed(toc_do)