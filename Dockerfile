FROM python:3.6-alpine
MAINTAINER Alejandro Bautista R.

ENV PYTHONUNBUFFERED 1

COPY ./Pipfile /Pipfile

# Run the following dependencies to get the most updated openssl
RUN apk --update add openssl ca-certificates py-openssl wget
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev build-base
RUN pip install pipenv
RUN pipenv lock
RUN pipenv install --ignore-pipfile

# Error [SSL:TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:661)
# Use the following command in terminal
# export COMPOSE_TLS_VERSION=TLSv1_2

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Create a user that runs our container
# -D means to create a user that only runs applications
RUN adduser -D user

#switch to the User instead of letting the root user to run it
USER user