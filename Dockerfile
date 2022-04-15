FROM python:3.8-slim

RUN apt-get update && apt-get install vim nano htop curl wget -y

WORKDIR /app

ADD requirements.txt .

RUN pip3 install -r requirements.txt

ADD . .

