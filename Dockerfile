FROM python:3.7-alpine

MAINTAINER ash_360 

# Doesnt allow python to buffer the output thus saving us precious memory and CPU
ENV PYTHONUNBUFFERED 1

# Install dependencies from requirements.txt file
# Source to Destination 
COPY ./requirements.txt /requirements.txt

# Inside the docker image in the root folder run pip command
RUN pip install -r /requirements.txt

# Creates empty folder inside docker
RUN mkdir /app


# Sets new folder as our working directory
WORKDIR /app

# Copy our code from current folder to docker
COPY ./app /app


# Its important to add another user with lesser permissions than root since if our system
# gets compromised the user wont have all the permissions to run the app
RUN adduser -D user

# Switch to our new user
USER user







