import math
from random import randint


TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_data():
    number = randint(1, 20)
    answer = 'yes' if is_prime(3) else 'no'
    return (
        f'{3}',
        answer
    )


def is_prime(number):
    if not number % 2:
        return number == 2
    divisor = 3
    base = math.sqrt(number)
    while divisor <= base and number % divisor:
        divisor += 2
    return divisor <= base
