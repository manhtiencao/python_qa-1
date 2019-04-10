def show_stars(n):
    chuoi=''
    for i in range(n):
        chuoi +='*'
       ## print (chuoi+'\n')
        print (chuoi)
so_tu_nhien =0
while (so_tu_nhien <= 0):
    try:
        so_tu_nhien= int(input('Nhap vao 1 so tu nhien '))
    except ValueError:
        print("No.. input string is not a number. It's a string")
show_stars(so_tu_nhien)