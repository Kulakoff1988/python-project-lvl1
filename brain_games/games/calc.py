from random import randint, choice
from brain_games.engine import engine


def run():
    game_description = 'What is the result of the expression?'

    def game_data():
        first_number = randint(1, 20)
        second_number = randint(1, 20)
        operators = ['+', '-', '*']
        operator = choice(operators)
        if operator == '+':
            answer = str(first_number + second_number)
        if operator == '-':
            answer = str(first_number - second_number)
        if operator == '*':
            answer = str(first_number * second_number)
        return {
            'question': f'{first_number} {operator} {second_number}',
            'answer': answer
        }

    engine(game_description, game_data)
