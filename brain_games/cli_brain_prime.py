import prompt
import random


def prime():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    j = 1
    while j <= 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        if number > 1:
            for i in range(2, (number // 2) + 1):
                if number % i == 0:
                    result = 'no'
                    break
            else:
                result = 'yes'
        else:
            result = 'yes'
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
        else:
            print(f"{answer} is wrong answer. Correct answer was {result}\nLet's try again, {name}!")
        j += 1
