# Используем официальный образ Python 3.11
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Выполняем миграции Alembic перед запуском приложения
CMD ["sh", "-c", "sleep 10 && alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8001"]
