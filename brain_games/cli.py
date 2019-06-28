import prompt

def run():
	name = prompt.string('Welcome to the Brain Games!\n\nMay I have your name? ')
	print('Hello, {}!'.format(name))
