import math
from random import randint


TITLE = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def get_round():
    number = randint(1, 20)
    answer = "yes" if is_prime(number) else "no"
    return (
        number,
        answer
    )


def is_prime(number):
    if not number % 2 or number < 2:
        return number == 2
    divisor = 3
    base = math.sqrt(number)
    while divisor < base and number % divisor:
        divisor += 2
    return divisor > base
