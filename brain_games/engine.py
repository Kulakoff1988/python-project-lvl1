from brain_games.cli import player_greeting, get_player_name, get_player_answer


def run(game_description, game_data):
    print_game_title(game_description)
    PLAYER_NAME = get_player_name()

    print_game_process(PLAYER_NAME, game_data)


def print_game_title(game_description):
    player_greeting()
    print(f'{game_description}\n\n')


def print_game_process(PLAYER_NAME, game_data):
    correct_answers = 0
    while correct_answers < 3:
        GAME_DATA = game_data()
        question = GAME_DATA['question']
        print(f'Question: {question}')
        RIGHT_ANSWER = GAME_DATA['answer']
        PLAYER_ANSWER = get_player_answer()
        if PLAYER_ANSWER == RIGHT_ANSWER:
            print('Correct!')
            correct_answers += 1
        else:
            PART_ONE = f'"{PLAYER_ANSWER}" is wrong answer ;(. '
            PART_TWO = f'Correct answer was "{RIGHT_ANSWER}".'
            print(PART_ONE + PART_TWO)
            print(f'Let\'s try again, {PLAYER_NAME}!')
            return
    print(f'Congratulations, {PLAYER_NAME}!')
