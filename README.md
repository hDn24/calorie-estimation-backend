# Salad detection

Supports:

- [x] Check CI with github actions
- [x] flake8, mypy, precommit

# How to start `pre-commit`

0. `pre-commit install`
1. `pre-commit run --all-files`

# How to start API

## Create virtual environment:

- `virtualenv env`
- `source env/bin/activate`

## Install the required libs

- `pip install -r requirements.txt`

## Run API

- `python main.py`

## Docker
- `docker build --tag hdn24/food-detection .`
- `docker run --rm -it -p 5001:5000 hdn24/food-detection:latest`
- Open `http://localhost:5001/` to check api
