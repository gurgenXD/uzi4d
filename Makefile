PYTHONPATH = export PYTHONPATH=./
POETRY_RUN = poetry run


migrations-make: ## Создать миграцию базы данных.
	$(POETRY_RUN) python manage.py makemigrations

migrations-up: ## Накатить миграции.
	$(POETRY_RUN) python manage.py migrate

migrations-down: ## Откатить последнюю миграцию.
	$(POETRY_RUN) python manage.py migrate

start-app: ## Запусть APP.
	$(POETRY_RUN) python manage.py runserver


lint: ## Проверить код.
	$(POETRY_RUN) black --check .
	$(POETRY_RUN) ruff check .

test: ## Запустить тесты.
	$(PYTHONPATH) && $(POETRY_RUN) pytest tests --cov=./ --cov-report html

format: ## Отформатировать все файлы.
	$(POETRY_RUN) black .
	$(POETRY_RUN) ruff check . --fix

docker-up: ## Запустить инфраструктуру для локальной разрабоки.
	docker-compose -f ./cicd/docker-compose.local.yml up -d
