from random import randint, choice
from brain_games import engine


def run():
    game_description = 'What is the result of the expression?'

    def game_data():
        first_number = randint(1, 20)
        second_number = randint(1, 20)
        operators = ['+', '-', '*']
        operator = choice(operators)
        answer = get_result(first_number, second_number, operator)
        return {
            'question': f'{first_number} {operator} {second_number}',
            'answer': answer
        }
    engine.run(game_description, game_data)


def get_result(number_one, number_two, operation):
    if operation == '+':
        answer = str(number_one + number_two)
    if operation == '-':
        answer = str(number_one - number_two)
    if operation == '*':
        answer = str(number_one * number_two)
    return answer
