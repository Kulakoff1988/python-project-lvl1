from random import randint
from brain_games.engine import engine


def run():
    game_description = 'Answer "yes" if number even otherwise answer "no".'

    def game_question():
        global random_nubmer
        random_number = randint(1, 100)
        return random_number

    def get_game_answer():
        return 'yes' if random_nubmer % 2 == 0 else 'no'

    engine(game_description, game_question, get_game_answer)
