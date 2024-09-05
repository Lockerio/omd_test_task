FROM python:3.12

ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY ./requirements.txt .

RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

RUN pip install --upgrade pip &&  python -m pip install -r requirements.txt

COPY ./alembic ./alembic
COPY ./app ./app
COPY ./alembic.ini .