import prompt
import math
import random


def gcd():
	name = prompt.string('May I have your name? ')  
	print(f'Hello, {name}')
	print('Find the greatest common divisor of given numbers.')
	i = 1
	while i <= 3:
		num_1 = random.randint(1, 100)
		num_2 = random.randint(1, 100)
		result = math.gcd(num_1, num_2)
		answer = prompt.string(f'Question: {num_1} {num_2}: ')
		if int(answer) == result:
			print('Correct!')
		else:
			print(f"{answer} is wrong answer. Correct answer "
			f"was {result}\nLet's try again, {name}!")
			break
		i += 1
		if i == 4:
			print(f'Congratulations, {name}!')
