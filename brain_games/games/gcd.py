from random import randint
from brain_games import engine
from brain_games.helpers import get_gcd


def run():
    TITLE = 'Find the greatest common divisor of given numbers.'

    def game_data():
        FIRST_NUMBER = randint(1, 100)
        SECOND_NUMBER = randint(1, 100)
        ANSWER = get_gcd.run(FIRST_NUMBER, SECOND_NUMBER)
        return {
            'question': f'{FIRST_NUMBER} {SECOND_NUMBER}',
            'answer': ANSWER
        }
    engine.run(TITLE, game_data)
