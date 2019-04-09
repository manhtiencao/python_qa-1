import math

# def print_integer_1(number):
#     tmp = ''
#     for x in range(1, number + 1):
#         tmp += ' ' + str(x)
#     return tmp


def get_my_number(num):
    my_num = 0
    for i in range(1, num+1):
        digits = int(math.log10(i))+i  # count number of digits in number
        print (digits)
        my_num = my_num * (10 ** digits) + i
    return my_num


if __name__ == '__main__':
    n = int(input("Please input n: "))
    # test = print_integer_1(n)
    test = get_my_number(n)
    print (test)