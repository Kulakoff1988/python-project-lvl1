import prompt


def player_greeting():
    print('\nWelcome to the Brain Games!')


def get_player_name():
    PLAYER_NAME = prompt.string('May I have your name? ')
    print(f'Hello, {PLAYER_NAME}!\n')
    return PLAYER_NAME


def get_player_answer():
    PLAYER_ANSWER = prompt.string('Your answer: ')
    return PLAYER_ANSWER
