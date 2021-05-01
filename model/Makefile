.PHONY: create build data lint test clean

build:
	poetry install

data: build
	poetry run python ./src/data/make_dataset.py

lint: build
	poetry run pre-commit run --all-files

test: build
	poetry run pytest ./tests/src

clean:
	find ./src -type f -name ".gitkeep" -delete
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
