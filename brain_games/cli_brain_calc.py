import prompt
import random
def calc():
	name = prompt.string('May I have your name? ')
	print(f'Hello, {name}!')
	print('What is the result of the expression?')
	i = 1
	while i <= 3:
		choice = random.choice('+' '-' '*')
		num_1 = random.randint(1, 100)
		num_2 = random.randint(1, 100)
		if choice == '+':
			result = num_1 + num_2
		elif choice == '-':
			result = num_1 - num_2
		elif choice == '*':
			result = num_1 * num_2
		print(f'Question: {num_1} {choice} {num_2}')
		answer = prompt.string('Your answer: ')
		if int(answer) == result:
			print('Correct')
		else:
			print(f"{answer} is wrong answer. Correct answer "
				  f"was {result}\nLet's try again, {name}!")
			break
		i += 1
		if i == 4:
			print(f"Congratulations, {name}!")
