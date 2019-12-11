<div style="text-align: center;">

# Project

![Python: 3.7](https://img.shields.io/badge/python-3.7-blue.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Manager: pipenv](https://img.shields.io/badge/manager-pipenv-brightgreen.svg)](https://github.com/pypa/pipenv)

</div>


## Getting Started
### :hammer: Installation
- Make sure Python 3.7 is available on your system
- Install pipenv on your system : `pip install pipenv` or `curl https://raw.githubusercontent.com/kennethreitz/pipenv/master/get-pipenv.py | python`
- Create the virtual environment and install project packages `pipenv install --dev`
- Run the development setup script `pipenv run setup`

### :bulb: Useful `pipenv` commands

- Format the code `pipenv run format`
- Manually run the linter `pipenv run lint`
- Manually the tests `pipenv run test`
- Add a development package `pipenv install --dev <my-package>`
- Add a production package `poetry install <my-package>`
- Jump into the virtualenv to run custom commands `pipenv shell`
---