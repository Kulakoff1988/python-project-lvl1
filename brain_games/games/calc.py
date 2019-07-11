from random import randint, choice


title = 'What is the result of the expression?'


def game_data():
    first_number = randint(1, 20)
    second_number = randint(1, 20)
    operators = ['+', '-', '*']
    operator = choice(operators)
    answer = str(get_calc_result(first_number, second_number, operator))
    return (
        f'{first_number} {operator} {second_number}',
        answer
    )


def get_calc_result(first_number, second_number, operator):
    if operator == '+':
        return first_number + second_number
    if operator == '-':
        return first_number - second_number
    if operator == '*':
        return first_number * second_number
