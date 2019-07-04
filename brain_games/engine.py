from brain_games.cli import player_greeting, get_player_name, get_player_answer


def engine(game_description, game_data):
    player_greeting()
    print(f'{game_description}\n\n')
    name = get_player_name()

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
            print(f'"{player_answer}" is wrong answer ;(. Correct answer was "{right_answer}".')
            print(f'Let\'s try again, {name}!')

    print(f'Congratulations, {name}!')
