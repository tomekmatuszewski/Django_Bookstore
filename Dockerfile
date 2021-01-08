FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /bookstore
COPY requirements.txt /bookstore/
RUN pip install -r requirements.txt
COPY . /bookstore

