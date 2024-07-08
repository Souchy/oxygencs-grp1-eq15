## To implement
FROM python:3.11

WORKDIR /app

RUN pip install pipenv

COPY Pipfile .
RUN pipenv install

# COPY .env .
COPY src src

ENTRYPOINT pipenv run start
