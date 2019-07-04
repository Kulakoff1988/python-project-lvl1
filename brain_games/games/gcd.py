from random import randint
from brain_games.engine import engine


def run():
    game_description = 'Find the greatest common divisor of given numbers.'

    def game_data():
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        a = first_number
        b = second_number
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        answer = str(a + b)
        return {'question': f'{first_number} {second_number}', 'answer': answer}

    engine(game_description, game_data)
