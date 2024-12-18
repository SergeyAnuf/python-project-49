import random

import prompt


def progression():
    n = 1
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    while n <= 3:
        number_1 = random.randint(1, 20)
        numbers = [number_1]
        i = random.randint(6, 10)
        sub = random.randint(1, 10)
        number_next = number_1 + sub
        j = 1
        while j < i:
            numbers.append(number_next)
            j += 1
            number_next = number_next + sub
        k = random.randint(1, i - 1)
        numbers[k] = '..'
        print('What number is missing in the progression?')
        print('Question:', *numbers)
        answer = prompt.string('Your answer: ')
        if k == 1:
            numbers[k] = numbers[k + 1] - sub
        else:
            numbers[k] = numbers[k - 1] + sub
        sub = 0
        if int(answer) == numbers[k]:
            print('Correct!')
            n += 1
        else:
            print(f"{answer} is wrong answer. Correct answer "
            f"was {numbers[k]}\nLet's try again, {name}!")
            break
        if n == 4:
            print(f'Congratulations, {name}!')
