def fizz_buzz(n):
    if n % 3 == 0 & n % 5 == 0:
        return "Fizz & Buzz"
    elif n % 3 == 0:
        return"Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return "Opps"


if __name__ == '__main__':
    n = int(input("Please input n: "))
    _check_call = fizz_buzz(n)
    print(_check_call)