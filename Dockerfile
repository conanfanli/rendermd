FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install tree -y
RUN pip3 install rendermd

RUN mkdir /app
WORKDIR /app

ENV PYTHONPATH .

CMD [ "rendermd" ]
