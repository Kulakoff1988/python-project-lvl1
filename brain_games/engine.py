from brain_games.cli import player_greeting, get_player_name, get_player_answer


def engine(game_description, game_question, get_game_answer):
    player_greeting()
    print(f'{game_description}\n\n')
    name = get_player_name()

    correct_answers = 0
    while correct_answers < 3:
        question = game_question()
        print(f'Question: {question}')
        right_answer = get_game_answer()
        answer = get_player_answer()
        if answer == right_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{right_answer}".')
            print(f'Let\'s try again, {name}!')

    print(f'Congratulations, {name}!')
