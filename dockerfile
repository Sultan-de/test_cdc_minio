#Deriving the latest base image
FROM python:3.7-alpine
ADD . /code
WORKDIR /code


#Labels as key value pair
LABEL Maintainer="mukanov_s"

COPY test.py ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir kafka-python && \
    pip install --no-cache-dir minio && \
	pip install --no-cache-dir python-dotenv

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./test.py"]