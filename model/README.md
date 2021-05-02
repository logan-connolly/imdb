# Model Factory

Based on the following cookie cutter: https://github.com/drivendata/cookiecutter-data-science

# Prerequisites

Python >= 3.8 must be installed along with [Poetry](https://python-poetry.org/).

# Usage

The easiest way to trigger the pipeline is via `make`:

```shell
# Create local python venv enviroment
make create

# Retrieve and process data
make data

# Run Linting via pre-commit
make lint

# Run unittests
make test

# Clean up files in directory
make clean
```
