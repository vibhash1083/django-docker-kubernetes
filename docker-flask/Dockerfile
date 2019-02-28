FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

FROM python:3

WORKDIR /app
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
