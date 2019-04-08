while True:
    try:
        a = int(input("Please enter a number: "))
        if int(a) % 3 == 0 and int(a) % 5 == 0:
            print("Fizz Buzz")
        elif int(a) % 5 == 0:
            print("Buzzz")
        elif int(a) % 3 == 0:
            print("Fizzz")
        else:
            print("Opps")
        break
    except ValueError:
        print("Please enter a valid number!")