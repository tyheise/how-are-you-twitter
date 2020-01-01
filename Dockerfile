# Python 3.6 as parent image
FROM python:3.6.9-slim-buster

# make a directory for the app
RUN mkdir /app

# set that directory as the wroking directory
WORKDIR /app

# Copy all repo contents to that directory
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000
