# Calorie estimation

_Calorie estimation backend project_

_Supports_:

- [x] Check CI with github actions
- [x] flake8, mypy, precommit

## Based

- Python `3.8.0`
- pip `22.3.1`

## Libraries

- [*fastapi*](https://fastapi.tiangolo.com/) `0.109.1`
- [*tflite-runtime*](https://pypi.org/project/tflite-runtime/) `2.7.0`
- [*tflite-support*](https://pypi.org/project/tflite-support/) `0.4.3`

## Install (for development)

### Run `pre-commit`
*for check coding conventions*

```shell
$ pre-commit install
```

```shell
$ pre-commit run --all-files
```

### Build & run


*Make your own `.env` file from the example:*

```shell
$ cp .env.example .env
# update values
```

*Build and run the docker image*

```shell
$ make app
```

### API docs

*Now, you can view the API docs via `http://localhost:8001/docs`*
