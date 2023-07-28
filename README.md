# Deposit

FastAPI приложение для расчета депозита по месяцам

![Checkers](https://github.com/iamrustamov/interview/actions/workflows/code-checker.yaml/badge.svg)

## Установка

1. Установите Python 3.10 или более поздние версии.

2. Установите Poetry (если он ещё не установлен):
   ```bash
   curl -sSL https://install.python-poetry.org | python -

Или используйте [другие доступные способы установки Poetry](https://python-poetry.org/docs/#installation).

1. Склонируйте репозиторий проекта:
   ```bash
   git clone https://github.com/iamrustamov/interview.git
2. Перейдите в каталог проекта:
   ```bash
   cd interview
3. Активируйте виртуальное окружение Poetry с помощью команды:
   ```bash
   poetry shell
4. Установите зависимости с помощью Poetry:
   ```bash
   poetry install

Теперь проект успешно установлен и готов к запуску.

## Запуск проекта

1. Запустите сервер FastAPI с помощью Poetry:
   ```bash
   poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
   Здесь `app.main:app` указывает путь к экземпляру FastAPI. Замените его на свой путь, если у вас есть другой входной модуль.
2. Теперь сервер FastAPI запущен и доступен по адресу http://localhost:8000. Вы можете протестировать различные эндпоинты с помощью Swagger UI или ReDoc, которые предоставляются FastAPI.

## Запуск проекта в Docker

1. Постройте Docker-образ из Dockerfile:
   ```bash
   docker build -t your-image-name .
   ```
   Здесь `your-image-name` - имя, которое вы хотите присвоить своему Docker-образу.
2. Запустите контейнер из построенного Docker-образа:
   ```bash
   docker run -d -p 8000:8000 your-image-name
   ```
   Контейнер будет запущен и доступен по адресу http://localhost:8000.

   Теперь FastAPI проект успешно запущен в Docker-контейнере.

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT.
