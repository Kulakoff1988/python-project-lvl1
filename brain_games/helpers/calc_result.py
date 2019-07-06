def run(first_number, second_number, operator):
    if operator == '+':
        ANSWER = str(first_number + second_number)
    if operator == '-':
        ANSWER = str(first_number - second_number)
    if operator == '*':
        ANSWER = str(first_number * second_number)
    return ANSWER
