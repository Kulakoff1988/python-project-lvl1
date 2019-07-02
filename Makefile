all: install
install:
	@python3 -m poetry install
lint:
	@python3 -m poetry run flake8 brain_games --ignore=E501 --count
