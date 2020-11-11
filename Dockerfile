#./Dockerfile
FROM python:3.8
WORKDIR /usr/src/app

## Install packages
COPY requirements.txt ./
RUN pip install -r requirements.txt

## Copy all src files
COPY . .

## Run the application on th port 8000
EXPOSE 8000

## CMD
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "tpay.wsgi:application"]
