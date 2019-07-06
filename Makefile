all: install
install:
	@python3 -m poetry install
lint:
	@python3 -m poetry run flake8 brain_games --count
package_install:
	@pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.test.org/simple/ kulakoff2803-brain-games