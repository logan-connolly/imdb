#################################################################################
# GLOBALS                                                                       #
#################################################################################

BASE_PYTHON = python3
PIP = ./venv/bin/pip
PYTHON = ./venv/bin/python
PRECOMMIT = ./venv/bin/pre-commit

#################################################################################
# COMMANDS                                                                      #
#################################################################################

create_venv:
	$(BASE_PYTHON) -m venv venv
	$(PIP) install -U pip setuptools wheel
	$(PIP) install -r requirements.txt

build:
	$(PIP) install -e .

data: build
	$(PYTHON) ./src/data/make_dataset.py

lint: build
	$(PRECOMMIT) run --all-files

unittests: build
	$(PYTHON) -m pytest ./tests/src

clean:
	find ./src -type f -name ".gitkeep" -delete
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
