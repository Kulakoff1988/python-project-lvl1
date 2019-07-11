from random import randint


title = 'Find the greatest common divisor of given numbers.'


def game_data():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    answer = str(get_gcd(first_number, second_number))
    return (
        f'{first_number} {second_number}',
        answer
    )


def get_gcd(first_number, second_number):
    while first_number and second_number:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    return first_number + second_number
