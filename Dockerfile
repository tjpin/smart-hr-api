FROM python:3.10.13-slim-bullseye
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8000

