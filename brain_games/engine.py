from brain_games.cli import get_player_greeting
from brain_games.cli import get_player_name, get_player_answer


def run(game):
    print_game_title(game)
    player_name = get_player_name()

    run_game_process(player_name, game)


def print_game_title(game):
    get_player_greeting()
    print(f'{game.title}')
    print()
    print()


def run_game_process(player_name, game):
    correct_answers = 0
    while correct_answers < 3:
        game_data = game.game_data()
        (question, right_answer) = game_data
        print(f'Question: {question}')
        player_answer = get_player_answer()
        if player_answer == right_answer:
            print('Correct!')
            correct_answers += 1
        else:
            string = (
                f'"{player_answer}" is wrong answer ;(. '
                f'Correct answer was "{right_answer}".'
            )
            print(string)
            print(f'Let\'s try again, {player_name}!')
            return
    print(f'Congratulations, {player_name}!')
