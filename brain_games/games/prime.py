from random import randint
from brain_games import engine


def run():
    TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    def game_data():
        NUMBER = randint(1, 20)
        ANSWER = 'yes' if (isPrime(NUMBER)) else 'no'
        return {
            'question': f'{NUMBER}',
            'answer': ANSWER
        }
    engine.run(TITLE, game_data)


def isPrime(number):
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor ** 2 <= number and number % divisor != 0:
        divisor += 2
    return divisor ** 2 > number
