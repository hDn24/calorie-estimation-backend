# Local development
.PHONY: app lint venv test

app:
	docker compose up -d --build --force-recreate app
	docker compose logs -f app

lint:
	python -m ruff check

# Environment
venv:
	python3 -m venv calorie_estimation_env
	source calorie_estimation_env/bin/activate && \
	python3 -m pip install pip setuptools wheel && \
	python3 -m pip install --upgrade pip && \
	python3 -m pip install -e .[dev] && \
	pre-commit install && \
	pre-commit autoupdate

# Test
test:
	python3 -m flake8 ./app ./tests
	python3 -m mypy ./app ./tests
	# https://stackoverflow.com/a/55095253
	python -m pytest -s --durations=0 --disable-warnings ./app/ tests/
