import prompt


greeting = 'Welcome to the Brain Games!'

def run():
    print(greeting + '\n\n')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))


def run_even():
    print(greeting + '\nAnswer "yes" if number even otherwise answer "no".\n\n')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
