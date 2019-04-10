def num_speed ():
    x = input("Input speed of driver: ")
    return x

a = num_speed()
if int(a) > 70 :
    b = ((int(a) - 70) // 5)
    c = (int(a) - 130)
    if b >= 12 and c > 0:
        print("License suspended")
    else:
        print("Point: ", b)
#    print("not ok")
else:
    print("Ok")