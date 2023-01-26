FROM python:3.8

WORKDIR /usr/src/app
ENV FLASK_APP=app

COPY ./app/requirements.txt ./

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
