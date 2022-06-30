# test_cdc_minio

Let’s try to understand change data capture design pattern using a very simple example.

## Project overview

Let’s assume our application uses a postgres database for its datastore and assume this has the holding table and our destination is a MiniO data store, we can store this as a simple json file in our local machine since this is a toy example. 

The reason why we chose json format, because commonly it is used for serializing and transmitting structured data over network connection.

## Design overview
![design_overview](https://user-images.githubusercontent.com/80713515/176095835-ff4ace08-9185-42e5-a11c-33af4eddf6a4.png)

## Requirements:
In order to follow along you will need the tools specified below

([Docker](https://docs.docker.com/get-docker/)) to run postgres, debezium,minio and kafka <br />
([Poetry](https://github.com/python-poetry/poetry)) Dependency Management for Python

## Quick Start
* Clone or download this repository
* Go inside of directory,  `cd test_cdc_minio`
* Run this command `docker-compose pull; docker-compose up`
* This docker-compose contains all the images which we will need in our project.
* Wait until it builds fully. All configurations are written in yml file.
* After service is built we can check for presence of connector: `curl -H "Accept:application/json" localhost:8083/connectors/`
* We can see the sde-connector is registered.
* Now we can start our python script insert.py to populate amount of data. Script inserts every 3 seconds to table a new data.
* Run this command in Terminal: 
```
poetry run python3 insert.py
```
* The poetry will take care of dependencies in our python script.
* After this we can visit MiniO console, [localhost:9000/](http://localhost:9001/buckets) `login:minioadmin; password:minioadmin;`
* We can check, that our python service wraps every 10 messages from kafka topic to one json file and saves it in MiniO bucket.



