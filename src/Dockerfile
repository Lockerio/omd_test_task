FROM python:3.12

ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY ./requirements.txt .

RUN pip install --upgrade pip &&  python -m pip install -r requirements.txt

COPY ./alembic ./alembic
COPY ./app ./app
COPY ./alembic.ini .