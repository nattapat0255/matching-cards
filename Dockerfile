FROM python:3.7

RUN pip3 install --upgrade pip

WORKDIR /usr/src/matching-card

COPY ./matching-card /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt