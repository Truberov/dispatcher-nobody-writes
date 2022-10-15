FROM python:latest
ENV PYTHONUNBUFFERED 1
ENV TZ 'Europe/Moscow'
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./customer_dispatcher_api/ .
EXPOSE 8000