import prompt

greeting = 'Welcome to the Brain Games!'


def run():
    print(greeting + '\n')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
