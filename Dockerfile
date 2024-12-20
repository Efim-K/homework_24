FROM python:3.12-slim

WORKDIR /app
# RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
# Копируем только файл с зависимостями
COPY pyproject.toml poetry.lock ./
# Устанавливаем Poetry и зависимости
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root

# гарантирует использование конкретной версии Poetry
# ENV POETRY_VERSION=1.8.2
# установленный в 1, предотвращает создание .pyc файлов
ENV PYTHONDONTWRITEBYTECODE=1
# установленный в 1, отключает буферизацию стандартного вывода
ENV PYTHONUNBUFFERED=1

# непонятно нужно или нет
COPY . .

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

