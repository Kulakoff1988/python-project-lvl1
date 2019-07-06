all: install
install:
	@python3 -m poetry install
lint:
	@python3 -m poetry run flake8 brain_games --count
package_uninstall:
	@pip uninstall kulakoff2803-brain-games
