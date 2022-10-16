#day 18 of 100-days-of-code
print("Guess my number between 0 - 1,000,000")

correct_number = 42
attempt = 1 

while True:
	guess =int(input("Guess my number: "))
	if guess < 0:
		print("Now we'll never know that the answer is...")
		exit()
	elif guess < correct_number:
		print("That number is too low. Try again!")
		attempt += 1
	elif guess > correct_number:
		print("That number is too low. Try again!")
		attempt += 1
	elif guess == correct_number:
		print("You are a winner!!")
		break
	else:
		print("Input Unkown")
print("It took you", attempt, "to get the right answer!!")
