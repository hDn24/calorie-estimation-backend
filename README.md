# Calorie estimation

_Calorie estimation backend project_

_Supports_:

- [x] Check CI with github actions
- [x] flake8, mypy, precommit

## Based

- Python `3.8.0`
- pip `22.3.1`

## Libraries

- [flask](https://flask.palletsprojects.com/en/2.2.x/) `2.2.3`
- [tflite-runtime](https://pypi.org/project/tflite-runtime/) `2.7.0`
- [tflite-support](https://pypi.org/project/tflite-support/) `0.4.3`

## Install (for development)

### Clone the project

```shell
git clone git@github.com:hDn24/calorie-estimation-backend.git
```

### Install the requirements and make environment

_Create virtual environment_

```shell
virtualenv env
```

```shell
source env/bin/activate
```

_Install the requirements_

```shell
cd calorie-estimation-backend
pip install -r requirements.txt
```

### Run `pre-commit`

```shell
pre-commit install
```

```shell
pre-commit run --all-files
```

### Start server

```shell
docker build --tag hdn24/calorie-estimation .
```

```
docker run --rm -it -p 8001:8000 hdn24/calorie-estimation:latest
```

### API docs

*Open `http://localhost:8001/docs` for API docs*
