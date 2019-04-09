#----------bAI4-----------
x = input(" Nhap speed : ")
if int(x) <= 70:
    print("OK")
else:
    a = (int(x) - 70) / 5
    if a <= 12:
        print('Point:', int(a))
    else:
        print('License suspended')
