FROM python:3.7.3-stretch
ENV PYTHONUNBUFFERED 1
WORKDIR /virtual_sensor
COPY . /virtual_sensor
RUN pip install --upgrade pip && pip install -r requirements.txt