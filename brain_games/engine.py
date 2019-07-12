from brain_games import cli


def run(game=None):
    if not game:
        greet_player()
        return
    introduce(game)
    player_name = cli.get_player_name()
    run_game_process(player_name, game)


def greet_player():
    print()
    print("Welcome to the Brain Games!")


def introduce(game):
    greet_player()
    print(game.TITLE)
    print()
    print()


def run_game_process(player_name, game):
    correct_answers = 0
    while correct_answers < 3:
        (question, right_answer) = game.game_data()
        print(f"Question: {question}")
        player_answer = cli.get_player_answer()
        if player_answer == right_answer:
            print("Correct!")
            correct_answers += 1
        else:
            string = (
                f'"{player_answer}" is wrong answer ;(. '
                f'Correct answer was "{right_answer}".'
            )
            print(string)
            print(f"Let's try again, {player_name}!")
            return
    print(f"Congratulations, {player_name}!")
