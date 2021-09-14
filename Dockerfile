FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY ./app /app

