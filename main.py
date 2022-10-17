#day 18 of 100-days-of-code
print("Guess my number between 0 - 1,000,000")

import random
attempt = 1
correct_number = random.randint(1,1000000)
print(correct_number)#this is for bug fixing if you run the code you will see why

while True:
	guess =int(input("Guess my number: "))
	if guess < 0:
		print("Now we'll never know that the answer is...")
		exit()
	elif guess < correct_number:
		print("That number is too low. Try again!")
		attempt += 1
	elif guess > correct_number:
		print("That number is too high. Try again!")
		attempt += 1
	elif guess == correct_number:
		print("You are a winner!!")
		break
	else:
		print("Input Unkown")
print("It took you", attempt, "to get the right answer!!")