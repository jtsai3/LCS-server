FROM python:3.10-slim

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install the required Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./start-web /start-web
RUN sed -i 's/\r$//g' /start-web
RUN chmod +x /start-web