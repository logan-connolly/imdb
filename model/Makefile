#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
BASE_PYTHON = python3
PIP = ./venv/bin/pip
PYTHON = ./venv/bin/python
PRECOMMIT = ./venv/bin/pre-commit

#################################################################################
# COMMANDS                                                                      #
#################################################################################

create_venv:
	$(BASE_PYTHON) -m venv $(PROJECT_DIR)/venv
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
	find $(PROJECT_DIR)/src -type f -name ".gitkeep" -delete
	find $(PROJECT_DIR) -type f -name "*.py[co]" -delete
	find $(PROJECT_DIR) -type d -name "__pycache__" -delete
