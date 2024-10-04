FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /manager_project

COPY requirements.txt /manager_project/

RUN pip install -r requirements.txt

COPY . /manager_project/
