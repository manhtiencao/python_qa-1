def show_num ():
    x = input("nhập số n: ")
    return x

a = show_num()
for x in range(0,int(a)+1):
    if int(x) % 2 == 0 :
        print (x,"EVEN")
    else:
        print(x,"ODD")