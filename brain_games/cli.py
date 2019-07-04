import prompt


def player_greeting():
    print('\nWelcome to the Brain Games!')


def get_player_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    return name


def get_player_answer():
    answer = prompt.string('Your answer: ')
    return answer
