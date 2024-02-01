# syntax=docker/dockerfile:1
FROM python:3.12.1-alpine3.19

WORKDIR /fetch-app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]
