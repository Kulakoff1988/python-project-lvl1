import prompt
from random import randint

greeting = 'Welcome to the Brain Games!'


def run():
    print(greeting)
    print('\nAnswer "yes" if number even otherwise answer "no".\n\n')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')

    correct_answers = 0

    while correct_answers < 3:
        random_number = randint(1, 100)
        right_answer = 'yes' if random_number % 2 == 0 else 'no'
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{right_answer}".')
            print(f'Let\'s try again, {name}!')

    print(f'Congratulations, {name}!')
