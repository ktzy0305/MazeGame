FROM python:3

WORKDIR /src/app

COPY requirements.txt /src/app/requirements.txt
WORKDIR /src/app
RUN pip install -r requirements.txt
COPY . /src/app

# set display port to avoid crash
ENV DISPLAY=:99