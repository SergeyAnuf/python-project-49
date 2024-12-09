import prompt
import random

def even():
	name = prompt.string('May I have your name? ')
	print(f'Hello, {name}!')
	print('Answer "yes" if the number is even, otherwise answer "no".')
	i = 1
	while i <= 3:
		number = random.randint(1, 100)
		print(f'Question: {number}')
		answer = prompt.string('Your answer: ')
		if number % 2 == 0:
			if answer == 'yes':
				print('Correct')
			else:
				print(f"'no' is wrong answer. Correct answer was 'yes'\nLet's try again, {name}!")
				break
		else:
			if answer == 'no':
				print('Correct')
			else:
				print(f"'yes' is wrong answer. Correct answer was 'no'\nLet's try again, {name}!")
				break
		i += 1
	if i == 4:
		print(f"Congratulations, {name}!")
