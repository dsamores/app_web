build:
	docker-compose build

run:
	docker-compose up

test:
	docker build -t app-web-tests .
	docker run app-web-tests pytest --cov=app --cov-report term-missing --cov-fail-under=70

lint:
	docker build -t app-web-tests .
	docker run app-web-tests pylint .
	docker run app-web-tests flake8 .
