FROM python:3

ENV pythonunbuffered 1

RUN mkdir /src

WORKDIR /src

COPY requirements.txt /src/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /src/