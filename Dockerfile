#./Dockerfile
FROM python:3.8

RUN mkdir /code
WORKDIR /code

## Install packages
ADD requirements.txt /code/
RUN pip install -r requirements.txt

## Copy all src files
ADD . /code/
