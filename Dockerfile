# Dockerfile

FROM python:3.10-alpine
WORKDIR /app  
COPY . /app
RUN apk --update add redis 
RUN apk add --update docker openrc
RUN pip install -r requirements.txt
RUN rc-update add docker boot
