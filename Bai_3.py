n = int(input("Nhap n: "))
for i in range (0,n+1):
    if i % 2 == 0:
        print(i, "EVEN")
    else:
        print(i, "ODD")
    i = i+1