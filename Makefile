all: install
install:
	@python3 -m poetry install
lint:
	@python3 -m poetry run flake8 brain_games --count --ignore=W191,E117
