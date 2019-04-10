while True:
	try:
		n = int(input("Pls input your number:\n "))
		if n>0:
			for x in range(0, n + 1):
				if x % 2 == 0:
					print(x, "EVEN")
				else:
					print(x, "ODD")
			break
		print("Pls inter interger!\n")
	except Exception:
		print(" Your number is incorrect format!")
	continue
print(" Thanks for Your view and comment")