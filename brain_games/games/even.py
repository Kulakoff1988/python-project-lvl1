from random import randint


TITLE = "Answer 'yes' if number even otherwise answer 'no'."


def get_round():
    number = randint(1, 100)
    answer = "no" if number % 2 else "yes"
    return (number, answer)
