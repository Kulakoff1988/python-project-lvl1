from random import randint
from brain_games import engine


def run():
    title = 'Answer "yes" if number even otherwise answer "no".'

    def game_data():
        number = randint(1, 100)
        answer = 'yes' if number % 2 else 'no'
        return {number, answer}

    engine.run(title, game_data)
