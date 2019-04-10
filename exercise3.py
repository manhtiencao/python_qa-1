# 3. Write a function called showNumbers that takes a parameter called limit.
# It should print all the numbers between 0 and limit with a label to identify
# the even and odd numbers. For example, if the limit is 3, it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

i = 0
n = float(input("Nhập vào một số bất kỳ: "))
while i <= n:
    if i % 2 == 0:
        print(i, "EVEN")
        i = i + 1
    else:
        print(i, "ODD")
        i = i + 1
