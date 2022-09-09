.PHONY: install run lint

install:
	@pip install pipenv
	@pipenv install --python 3.10

run:
	@python manage.py runserver

db:
	@python manage.py migrate

lint:
	@flake8
