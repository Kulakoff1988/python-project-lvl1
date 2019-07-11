from random import randint


title = 'Answer "yes" if number even otherwise answer "no".'


def game_data():
    number = randint(1, 100)
    answer = 'no' if number % 2 else 'yes'
    return (number, answer)
