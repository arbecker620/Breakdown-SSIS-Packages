FROM python:3.11-slim-buster

WORKDIR /app

COPY . .
#ADD titanic /app/

#WORKDIR /app/API/PredictionEngine
RUN pip3 install -r requirements.txt
#COPY . .
