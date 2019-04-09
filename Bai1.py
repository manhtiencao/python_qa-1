#----- Bai 1
x = input("Nhap gia tri x :")
a = int(x) % 3
b = int(x) % 5
if int(x) == 0:
    print('x=0. End')
else:
    if (a == 0 and b == 0):
        print("FizzBuzz")
    elif a == 0:
        print('Fizz')
    elif b == 0:
        print('Buzz')
    else:
        print('')
