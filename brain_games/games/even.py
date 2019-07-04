from random import randint
from brain_games.engine import engine


def run():
    game_description = 'Answer "yes" if number even otherwise answer "no".'

    def game_data():
        random_number = randint(1, 100)
        answer = 'yes' if random_number % 2 == 0 else 'no'
        return {'question': random_number, 'answer': answer}

    engine(game_description, game_data)
