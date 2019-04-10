# Ex 2
# def show_start ():
#     x = input("nhập số dòng: ")
#     return x
# a = show_start()
# for x in range(1,int(a)+1):
#     print("x"*x)

# Ex 2.1
def show_start ():
    x = input("nhập số dòng: ")
    return x
a = show_start()

while int(a) != 0:
    for x in range(int(a)):
        print("x",end='')
    print("")
#    print("x")
    a = int(a) - 1


# def is_odd(a):
#     return bool(a & 1)