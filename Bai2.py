# ----------Bai 2-------
x = input(" Nhap gia tri : ")
i = 1
if int(x) > 0:
    while i <= int(x):
        print('*' * int(i))
        i = i + 1
else:
    print('nhap loi')
