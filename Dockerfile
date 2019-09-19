FROM python:3-alpine

COPY ./src /app
COPY ./db /db
COPY ./log /log
COPY ./requirements.txt /requirements.txt

WORKDIR /app

# RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev

# ENV LIBRARY_PATH=/lib:/usr/lib

RUN pip install -r /requirements.txt

EXPOSE 5000

ENV FLASK_APP=app
ENV MAIL_SERVER=mail
ENV MAIL_PORT=1025
ENV YANDEX_TRANSLATOR_KEY=enter-your-key

ENTRYPOINT ["flask"]

CMD ["db", "upgrade"]
CMD ["translate", "compile"]
CMD ["run", "--host=0.0.0.0", "--port=80"]
