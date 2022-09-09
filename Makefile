.PHONY: install run lint

install:
	@pip install pipenv
	@pipenv install --python 3.10

run:
	@python manage.py runserver

lint:
	@flake8
