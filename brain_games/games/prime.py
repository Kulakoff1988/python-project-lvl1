from random import randint
from brain_games import engine
from brain_games.helpers import is_prime


def run():
    TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    def game_data():
        NUMBER = randint(1, 20)
        ANSWER = 'yes' if (is_prime.run(NUMBER)) else 'no'
        return {
            'question': f'{NUMBER}',
            'answer': ANSWER
        }
    engine.run(TITLE, game_data)
