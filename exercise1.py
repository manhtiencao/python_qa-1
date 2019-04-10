# 1. Write a function called fizz_buzz that takes a number.
#  If the number is divisible by 3, print “Fizz”.
#  If it is divisible by 5, it should return “Buzz”.
#  If it is divisible by both 3 and 5, it should return “FizzBuzz”.
#  Otherwise, print “Opps”


n = float(input("Nhập vào một số bất kỳ: "))
# while n < 0:
#     print(n, "không phải là số dương, vui lòng nhập lại")
#     n = int(input("Nhập vào một số dương bất kỳ: "))

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 5 == 0:
    print("Buzz")
elif n % 3== 0:
    print("Fizz")
else:
    print("Opps")
