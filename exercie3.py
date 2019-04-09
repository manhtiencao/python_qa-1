limit =int (input("Hãy nhập vào 1 số limit: "))
i=0
while i <= limit:
    show_number = i%2
    if show_number == 0:
        print(str(i)+ " EVEN")
    else:
        print(str(i)+ " ODD")
    i=i+1