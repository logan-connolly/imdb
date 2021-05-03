.PHONY: create build data plots lint tests clean

build:
	poetry install

data: build
	poetry run python ./src/data/make_dataset.py

plots: build
	poetry run python ./src/visualization/visualize.py

lint: build
	poetry run pre-commit run --all-files

tests: build
	poetry run pytest ./tests/src

clean:
	find ./src -type f -name ".gitkeep" -delete
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
