import prompt


def get_player_name():
    player_name = prompt.string("May I have your name? ")
    print(f"Hello, {player_name}!")
    print()
    return player_name


def get_player_answer():
    player_answer = prompt.string("Your answer: ")
    return player_answer
