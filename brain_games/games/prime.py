from random import randint
from brain_games import engine


def run():
    title = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    def game_data():
        random_number = randint(1, 20)
        answer = 'yes' if (isPrime(random_number)) else 'no'
        return {
            'question': f'{random_number}',
            'answer': answer
        }
    engine.run(title, game_data)


def isPrime(number):
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor ** 2 <= number and number % divisor != 0:
        divisor += 2
    return divisor ** 2 > number
