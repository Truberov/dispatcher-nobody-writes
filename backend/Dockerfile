FROM python:latest

WORKDIR /code
COPY requirements.txt /code/
COPY ./customer_dispatcher_api/ .
RUN apt update && apt install -y libpq-dev gcc python3-dev musl-dev netcat
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
