FROM python:3-alpine

# RUN adduser -D blog

WORKDIR /app

# RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
# ENV LIBRARY_PATH=/lib:/usr/lib

COPY requirements.txt /requirements.txt
RUN ["pip", "install", "-r", "/requirements.txt"]

COPY ./src /app
COPY ./db /db
COPY ./log /log

ENV FLASK_APP=run

# RUN chown -R blog:blog ./
# USER blog

EXPOSE 5000

RUN ["flask", "db", "upgrade"]
RUN ["flask", "translate", "compile"]

ENTRYPOINT ["flask"]

CMD ["run", "--host=0.0.0.0", "--port=80"]
