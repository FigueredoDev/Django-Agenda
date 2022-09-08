.PHONY: lint

install:
	@pip install pipenv
	@pipenv install --python 3.10

lint:
	@flake8
