from random import randint


TITLE = "What number is missing in the progression?"


def game_data():
    sequence_step = randint(1, 10)
    sequence_start = randint(1, 50)
    hidden_position = randint(1, 10)
    return get_prog_data(sequence_start, sequence_step, hidden_position)


def get_prog_data(start, step, hidden_position):
    next_number = start
    sequence = ""
    answer = ""
    sequence_count = 1
    while sequence_count <= 10:
        if sequence_count == hidden_position:
            sequence += " .."
            answer = next_number
        else:
            sequence += f" {next_number}"
        next_number += step
        sequence_count += 1
    return (sequence, str(answer))
