# Описание проекта

Проект представляет собой шаблон для создания API на базе FastAPI с использованием базы данных PostgreSQL и моделей обработки текста.

# Используемые библиотеки

fastapi - фреймворк для создания API

uvicorn - ASGI сервер

transformers - библиотека для работы с моделями обработки текста

sqlalchemy - ORM для работы с базами данных

psycopg2-binary - драйвер для работы с PostgreSQL

asyncpg - асинхронный драйвер для работы с PostgreSQL

pydantic - библиотека для работы с валидацией данных

pydantic-settings - библиотека для работы с настройками

alembic - библиотека для работы с миграциями

tensorflow - библиотека для работы с моделями

tf-keras - библиотека для работы с моделями

## Установка зависимостей

Для установки зависимостей используйте `pip`:

```bash
pip install -r requirements.txt
```

# Запуск проекта
```bash
docker-compose up --build
```

# Не забудьте создать файл .env и .env.container
Я разделил переменные на два файла для удобства работы в контейнере и вне.
соответвственно у вас два образца:
.env.example
.env.container.example

# Работа с alembic

```bash
alembic init migrations
```
настраиваем env.py в папке migrations
потом:

```bash
alembic revision --autogenerate -m "0_Initial"
```
Применить миграции:

```bash
alembic upgrade head
```
