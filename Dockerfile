# образ на основе которого создаём контейнер
FROM python:3.10.4

# рабочая директория внутри проекта
WORKDIR /numbers

# переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для Postgre
RUN apt update && apt -y install postgresql-server-dev-all gcc python3-dev musl-dev libpq-dev nginx

# устанавливаем зависимости для Python
RUN pip install --upgrade pip
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install --upgrade setuptools
COPY ./requirements.txt .
#RUN pip install -r requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt
CMD ["python3", "manage.py", "fill_db", "&&", "python3", "manage.py", "update_run_processin","&&","python","manage.py","runserver"]

