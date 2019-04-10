while True:
    try:
        show_star = int(input('Input your number:'))
        for x in range(1, show_star+1):
            print('*'*x)
        break
    except Exception as err:
        print('error=%s', err)
        continue

