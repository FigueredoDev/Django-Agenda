.PHONY: install run db lint test

install:
	@pip install pipenv
	@pipenv install --python 3.10

run:
	@python manage.py runserver

db:
	@python manage.py migrate

lint:
	@flake8

test:
	@python manage.py test
