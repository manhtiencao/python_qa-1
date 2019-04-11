#EX4
speed = float(input("Enter value: "))
if speed <=70:
    print("ok")
else:
    overspeed = (speed -70)/5
    if overspeed<12:
        print("points:",round(overspeed,2))
    else:
        print("points: ", round(overspeed,2), 'License suspend')

