number = int(input ("Hãy nhập 1 số bất kỳ khác 0: "))
fizz = int(number)%3
buzz = int(number)%5
if (number == 0 or number < 0):

    print("Số bạn nhập không hợp lệ! ")
    n = int(input("Vui lòng nhập lại: "))
    fizz2 = int(n) % 3
    buzz2 = int(n) % 5
    if  (fizz2==0 and buzz2==0):
        print("Số vừa chia hết cho 3 và chia hết cho 5")
    elif (buzz2==0 and fizz2!=0):
        print("Số chia hết cho 5")
    elif (fizz2==0 and buzz2!=0):
        print("Số chia hết cho 3")

    else:
        print("Opps")

else:

    if  (fizz==0 and buzz==0):
        print("Số vừa chia hết cho 3 và chia hết cho 5")
    elif (buzz==0 and fizz!=0):
        print("Số chia hết cho 5")
    elif (fizz==0 and buzz!=0):
        print("Số chia hết cho 3")

    else:
        print("Opps")

