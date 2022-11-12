FROM python:3.10.7-alpine

# set work directory
WORKDIR ./thesombot_web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

# upgrade pip
RUN pip install --upgrade pip

# install dependensis
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev  \
    libc-dev linux-headers postgresql-dev && \
    pip install --no-cache-dir -r requirements.txt