while True:
    try:
        show_star = int(input('Input your number:'))
        if show_star > 0:
            for x in range(1, show_star+1):
                    print('*'*x)
            break
        print("Please Try Again")
        print("-"*30)

    except Exception as err:
        print("Error:", err)
        continue

