# 2. Write a function called show_stars(rows). If rows is 5, it should print the
# following:
# *
# **
# ***
# ****
# *****

i = 1
n = int(input("Nhập vào một số dương bất kỳ: "))

while n < 0:
    print(n, "không phải là số dương, vui lòng nhập lại")
    n = int(input("Nhập vào một số dương bất kỳ: "))

while i <= n:
    print(i * "*")
    i = i + 1
