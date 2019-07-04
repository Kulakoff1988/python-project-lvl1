from random import randint
from brain_games.engine import engine


def run():
    game_description = 'What number is missing in the progression?'

    def game_data():
        sequence_step = randint(1, 10)
        sequence_start = randint(1, 50)
        hidden_number = randint(1, 10)
        next_number = sequence_start
        sequence = ''
        answer = ''
        sequence_count = 0
        while sequence_count < 10:
            if sequence_count == hidden_number:
                sequence += f' ..'
                answer = str(next_number)
            else:
                sequence += f' {next_number}'
            next_number += sequence_step
            sequence_count += 1
        return {'question': sequence, 'answer': answer}

    engine(game_description, game_data)
