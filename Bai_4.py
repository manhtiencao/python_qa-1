speed = int(input("Input speed: "))
rang = 0
if speed < 70:
    print("OK")
else:
    for x in range (70,speed,5):
        rang = rang + 1
    if  rang < 12:
        print("Points: ", rang)
    else:
        print("License suspended")