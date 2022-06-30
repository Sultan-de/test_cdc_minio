#Deriving the latest base image
FROM python:3.7-alpine
ADD . /code
WORKDIR /code


#Labels as key value pair
LABEL Maintainer="mukanov_s"

COPY curl.sh ./
COPY test.py ./


ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait

RUN chmod +x /wait
RUN chmod +x ./curl.sh
RUN apk --update --no-cache add curl
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir kafka-python && \
    pip install --no-cache-dir minio && \
	pip install --no-cache-dir python-dotenv