from random import randint
from brain_games import engine


def run():
    TITLE = 'What number is missing in the progression?'

    def game_data():
        SEQUENCE_STEP = randint(1, 10)
        SEQUENCE_START = randint(1, 50)
        HIDDEN_POSITION = randint(1, 10)
        return get_game_data(SEQUENCE_START, SEQUENCE_STEP, HIDDEN_POSITION)
    engine.run(TITLE, game_data)


def get_game_data(start, step, hidden_position):
    next_number = start
    sequence = ''
    answer = ''
    sequence_count = 1
    while sequence_count <= 10:
        if sequence_count == hidden_position:
            sequence += f' ..'
            answer = str(next_number)
        else:
            sequence += f' {next_number}'
        next_number += step
        sequence_count += 1
    return {'question': sequence, 'answer': answer}
