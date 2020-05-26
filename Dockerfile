FROM python:3

ENV pythonunbuffered 1

RUN mkdir /src

WORKDIR /src

COPY requirements.txt /src/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /src/

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]