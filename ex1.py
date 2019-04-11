#EX1:
Number = input("enter your number: ")
while Number:
    if int(Number)%3==0:
        print("Fiz")
        break
    elif int(Number)%5==0:
        print("Buzz")
        break
    elif (int(Number)%3==0) and int(Number)%5==0:
        print("FizzBuzz")
        break
    else:
        print("Opps")
        break





