from brain_games.cli import player_greeting, get_player_name, get_player_answer


def run(game_description, game_data):
    print_game_title(game_description)
    player_name = get_player_name()

    print_game_process(player_name, game_data)


def print_game_title(game_description):
    player_greeting()
    print(f'{game_description}\n\n')


def print_game_process(player_name, game_data):
    correct_answers = 0
    while correct_answers < 3:
        data = game_data()
        question = data['question']
        print(f'Question: {question}')
        right_answer = data['answer']
        player_answer = get_player_answer()
        if player_answer == right_answer:
            print('Correct!')
            correct_answers += 1
        else:
            part_one = f'"{player_answer}" is wrong answer ;(. '
            part_two = f'Correct answer was "{right_answer}".'
            print(part_one + part_two)
            print(f'Let\'s try again, {player_name}!')
            return
    print(f'Congratulations, {player_name}!')
