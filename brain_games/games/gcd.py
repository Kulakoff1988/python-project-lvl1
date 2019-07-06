from random import randint
from brain_games import engine


def run():
    TITLE = 'Find the greatest common divisor of given numbers.'

    def game_data():
        FIRST_NUMBER = randint(1, 100)
        SECOND_NUMBER = randint(1, 100)
        ANSWER = get_gcd(FIRST_NUMBER, SECOND_NUMBER)
        return {
            'question': f'{FIRST_NUMBER} {SECOND_NUMBER}',
            'answer': ANSWER
        }
    engine.run(TITLE, game_data)


def get_gcd(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    return str(first_number + second_number)
