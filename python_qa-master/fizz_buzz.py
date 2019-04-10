while True:
    try:
        fizz_buzz = int(input('Input your number:'))
        if fizz_buzz % 3 == 0 and fizz_buzz % 5 == 0:
            print('FizzBuzz')
        elif fizz_buzz % 3 == 0:
            print("Fizz")
        elif fizz_buzz % 5 == 0:
            print("Buzz")
        else:
            print("Opps")
        break
    except Exception as err:
            print('Error:', err)
            print("-"*30)
    continue
