from random import randint
from brain_games.engine import engine


def run():
    game_description = 'Find the greatest common divisor of given numbers.'

    def game_data():
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        answer = get_gcd(first_number, second_number)
        return {
            'question': f'{first_number} {second_number}',
            'answer': answer
        }

    def get_gcd(number_one, number_two):
        while number_one != 0 and number_two != 0:
            if number_one > number_two:
                number_one %= number_two
            else:
                number_two %= number_one
        return str(number_one + number_two)

    engine(game_description, game_data)
