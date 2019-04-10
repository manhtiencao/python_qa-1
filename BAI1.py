def fizz_buzz(n):

        if (n % 3 ==0 and n % 5 != 0 ):
            print('Fizz ')
        elif   (n % 5 ==0 and n % 3 !=0 ):
            print('Buzz ')
        elif (n % 5 == 0 and n % 3 ==0):
            print('FizzBuzz ')
        else:
            print('Opps ')
so_tu_nhien =0
while (so_tu_nhien <= 0 ):
    try:
        so_tu_nhien= int(input('Nhap vao 1 so tu nhien '))
    except ValueError:
        print("No.. input string is not a number. It's a string")
fizz_buzz(so_tu_nhien)


