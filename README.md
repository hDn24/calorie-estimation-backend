# Calorie estimation
Calorie estimation backend project

Supports:

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
### Get project by git clone

```
git clone git@github.com:hDn24/calorie-estimation-backend.git
```

### Install the requirements and make environment
 Create virtual environment
```shell
virtualenv env
```
```shell
source env/bin/activate
```
Install the requirements
```shell
cd calorie-estimation-backend
pip install -r requirements.txt
```

### Run `pre-commit`

```
pre-commit install
```

```
pre-commit run --all-files
```

### Start server

```shell
docker build --tag hdn24/calorie-estimation .
```

```
docker run --rm -it -p 5001:5000 hdn24/calorie-estimation:latest
```

### API docs

- Open `http://localhost:5001/` to check api
  - GET: `http://localhost:5001/` Health check api
  - POST: `http://localhost:5001/detect` Detect api
    - key: file[] (type: `file`)
    - value: Choose a file from local
