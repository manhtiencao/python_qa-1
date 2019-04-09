#-------Bai 3-----------
x = input(" Nhap gia tri : ")
i = 0
if int(x) > 0:
    while i <= int(x):
        if (int(i) % 2) == 0:
            print(i, '', 'EVEN')
        else:
            print(i, '', 'ODD')
        i = i+1
else:
    print('nhap lôi')

