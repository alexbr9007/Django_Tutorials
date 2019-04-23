FROM python:3.6-alpine
MAINTAINER Alejandro Bautista R.

ENV PYTHONUNBUFFERED 1

COPY ./Pipfile /Pipfile
RUN pip install pipenv
RUN pipenv lock
RUN pipenv install --ignore-pipfile


RUN mkdir/app
WORKDIR /app
COPY ./app /app

# Create a user that runs our container
# -D means to create a user that only runs applications
RUN adduser -D user

#switch to the User instead of letting the root user to run it
USER user