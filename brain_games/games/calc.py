from random import randint, choice
from brain_games import engine


def run():
    TITLE = 'What is the result of the expression?'

    def game_data():
        FIRST_NUMBER = randint(1, 20)
        SECOND_NUMBER = randint(1, 20)
        OPERATORS = ['+', '-', '*']
        OPERATOR = choice(OPERATORS)
        ANSWER = get_result(FIRST_NUMBER, SECOND_NUMBER, OPERATOR)
        return {
            'question': f'{FIRST_NUMBER} {OPERATOR} {SECOND_NUMBER}',
            'answer': ANSWER
        }
    engine.run(TITLE, game_data)


def get_result(first_number, second_number, operator):
    if operator == '+':
        ANSWER = str(first_number + second_number)
    if operator == '-':
        ANSWER = str(first_number - second_number)
    if operator == '*':
        ANSWER = str(first_number * second_number)
    return ANSWER
