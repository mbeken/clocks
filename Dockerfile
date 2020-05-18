from alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app
COPY . /app

RUN pip3 --no-cache-dir install -r req.lib.txt

RUN pylint app.py
RUN pytest clock_unittest.py

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]
