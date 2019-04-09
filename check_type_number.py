def show_number(number):
    col = {}
    for item in range(number+1):
        if item % 2 == 0:
            num = item
            type = "EVEN"
            col.update({num: type})
        else:
            num = item
            type = "ODD"
            col.update({num: type})
    return col


if __name__ == '__main__':
    number = int(input("Please input n: "))
    _check_odd_even = show_number(number)
    print(_check_odd_even)
