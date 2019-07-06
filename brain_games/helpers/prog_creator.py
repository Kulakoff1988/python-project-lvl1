def run(start, step, hidden_position):
    next_number = start
    sequence = ''
    answer = ''
    sequence_count = 1
    while sequence_count <= 10:
        if sequence_count == hidden_position:
            sequence += f' ..'
            answer = str(next_number)
        else:
            sequence += f' {next_number}'
        next_number += step
        sequence_count += 1
    return {'question': sequence, 'answer': answer}
