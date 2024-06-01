# Inherit from a base image
FROM python:3.12-slim

# Setting working directory
WORKDIR /app

#  Update pip version
RUN pip install --upgrade pip

# Copy requirements file
COPY requirements.txt requirements.txt

# Install packages
RUN pip install -r requirements.txt

# Copy the rest of project
COPY . .

# Set env variables
ENV PYTHONUNBUFFERED=1
