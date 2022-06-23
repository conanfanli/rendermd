FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN pip3 install rendermd

RUN mkdir /app
WORKDIR /app

ENV PYTHONPATH .

CMD [ "rendermd" ]
