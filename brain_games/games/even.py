from random import randint
from brain_games import engine


def run():
    TITLE = 'Answer "yes" if number even otherwise answer "no".'

    def game_data():
        NUMBER = randint(1, 100)
        ANSWER = 'yes' if NUMBER % 2 == 0 else 'no'
        return {'question': NUMBER, 'answer': ANSWER}

    engine.run(TITLE, game_data)
