FROM python:3.11.5-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /myair_app

WORKDIR /myair_app

RUN apt update -y && \
    apt install -y python3-dev \
    gcc \
    musl-dev \
    libpq-dev \
    nmap

ADD poetry.lock pyproject.toml /myair_app/

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

WORKDIR /src

COPY src /src

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
