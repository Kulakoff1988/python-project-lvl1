import math
from random import randint
from brain_games import engine


def run():
    title = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    def game_data():
        number = randint(1, 20)
        answer = 'yes' if is_prime(number) else 'no'
        return {
            f'{number}',
            answer
        }
    engine.run(title, game_data)


def is_prime(number):
    if number % 2 == 0:
        return number == 2
    divisor = 3
    base = math.sqrt(number)
    while divisor >= base and number % divisor != 0:
        divisor += 2
    return divisor <= base
