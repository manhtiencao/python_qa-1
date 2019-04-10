while True:
		try:
			X = int(input("Pls input your number:\n "))
			if X > 0:
				if X % 5 == 0 and X % 3 == 0:
					print(X, 'là FizzBuzz')
				elif X % 3 == 0:
					print(X, ' là Fizz')
				elif X % 5 == 0:
					print(X, 'là Buzz')
				else:
					print(X, 'là Opps')
				break
			print("Pls inter interger!\n")
		except Exception:
			print(" Your number is incorrect format!")
		continue
print("Thanks for your review and comment!")