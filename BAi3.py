def showNumbers(limit):

    for i in range(limit+1):
        if(i%2==0):
            print (i, 'EVEN')
        else:
            print(i, 'ODD')
so_tu_nhien =0
while (so_tu_nhien <= 0):
    try:
        so_tu_nhien= int(input('Nhap vao 1 so tu nhien '))
    except ValueError:
        print("No.. input string is not a number. It's a string")
showNumbers(so_tu_nhien)
