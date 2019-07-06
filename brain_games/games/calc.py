from random import randint, choice
from brain_games import engine
from brain_games.helpers import calc_result


def run():
    TITLE = 'What is the result of the expression?'

    def game_data():
        FIRST_NUMBER = randint(1, 20)
        SECOND_NUMBER = randint(1, 20)
        OPERATORS = ['+', '-', '*']
        OPERATOR = choice(OPERATORS)
        ANSWER = calc_result.run(FIRST_NUMBER, SECOND_NUMBER, OPERATOR)
        return {
            'question': f'{FIRST_NUMBER} {OPERATOR} {SECOND_NUMBER}',
            'answer': ANSWER
        }
    engine.run(TITLE, game_data)
