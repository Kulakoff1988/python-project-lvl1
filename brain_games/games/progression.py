from random import randint
from brain_games import engine
from brain_games.helpers import prog_creator


def run():
    TITLE = 'What number is missing in the progression?'

    def game_data():
        SEQUENCE_STEP = randint(1, 10)
        SEQUENCE_START = randint(1, 50)
        HIDDEN_POSITION = randint(1, 10)
        return prog_creator.run(SEQUENCE_START, SEQUENCE_STEP, HIDDEN_POSITION)
    engine.run(TITLE, game_data)
