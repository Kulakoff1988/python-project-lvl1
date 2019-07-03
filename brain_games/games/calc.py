from random import randint, choice
from brain_games.engine import engine


def run():
    game_description = 'What is the result of the expression?'

    def game_question():
        global operator
        global first_number
        global second_number
        first_number = randint(1, 20)
        second_number = randint(1, 20)
        operators = ['+', '-', '*']
        operator = choice(operators)
        return f'{first_number} {operator} {second_number}'

    def get_game_answer():
        if operator == '+':
            return str(first_number + second_number)
        if operator == '-':
            return str(first_number - second_number)
        if operator == '*':
            return str(first_number * second_number)

    engine(game_description, game_question, get_game_answer)
