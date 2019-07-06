def run(number):
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor ** 2 <= number and number % divisor != 0:
        divisor += 2
    return divisor ** 2 > number
