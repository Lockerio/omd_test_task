FROM python:3.12

ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY ./requirements.txt .

RUN apt-get update && apt-get install -y wget gnupg unzip

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable


RUN pip install --upgrade pip &&  python -m pip install -r requirements.txt

COPY ./alembic ./alembic
COPY ./app ./app
COPY ./alembic.ini .