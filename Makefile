SHELL = /bin/bash

# Environment
venv:
	python3 -m venv salad_detection_env
	source salad_detection_env/bin/activate && \
	python3 -m pip install pip setuptools wheel && \
	python3 -m pip install --upgrade pip && \
	python3 -m pip install -e .[dev] && \
	pre-commit install && \
	pre-commit autoupdate


# Style
style:
	black .
	flake8 salad_detection/
	python3 -m isort -rc salad_detection/

# Test
test:
	python3 -m flake8 ./salad_detection ./tests
	python3 -m mypy ./salad_detection ./tests
	# https://stackoverflow.com/a/55095253
	python -m pytest -s --durations=0 --disable-warnings ./salad_detection/ tests/
