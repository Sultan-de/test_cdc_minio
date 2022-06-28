# test_cdc_minio

Let’s try to understand change data capture design pattern using a very simple example.

## Project overview

Let’s assume our application uses a postgres database for its datastore and assume this has the holding table and our destination is a MiniO data store, we can store this as a simple json file in our local machine since this is a toy example. 

The reason why we chose json format, because commonly it is used for serializing and transmitting structured data over network connection.

## Design overview
![design_overview](https://user-images.githubusercontent.com/80713515/176095835-ff4ace08-9185-42e5-a11c-33af4eddf6a4.png)

## Requirements:
In order to follow along you will need the tools specified below
[TEXT TO SHOW](actual URL to navigate)

([Docker](https://docs.docker.com/get-docker/)) to run postgres, debezium,minio and kafka <br />
([pgcli](https://github.com/dbcli/pgcli)) to connect to our postgres instance

## Quick Start
* Clone or download this repository
* Go inside of directory,  `cd test_cdc_minio`
* Run this command `docker-compose pull; docker-compose up`
* This docker-compose contains all the images which we will need in our project.
* Wait until it builds fully.
* After this, let’s create the data in postgres. We use pgcli to interact with our postgres instance
* Open new Terminal in current directory and Run this command `pgcli -h localhost -p 5432 -U start_data_engineer` #password is password
* After connect to DB, run this command: 
```sql
CREATE SCHEMA bank;
SET search_path TO bank,public;
CREATE TABLE bank.holding (
    holding_id int,
    user_id int,
    holding_stock varchar(8),
    holding_quantity int,
    datetime_created timestamp,
    datetime_updated timestamp,
    primary key(holding_id)
);
ALTER TABLE bank.holding replica identity FULL;
\q
```
* The above is standard sql, with the addition of replica identity. This field has the option of being set as one of DEFAULT, NOTHING, FULL and INDEX which determines the amount of detailed information written to the WAL. We choose FULL to get all the before and after data for CRUD change events in our WAL, the INDEX option is the same as full but it also includes changes made to indexes in WAL which we do not require for our project’s objective. We also insert a row into the holding table.
* After this We have to register a debezium connect service using a curl command to the connect service on port 8083
* Run this command 
```
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" \
localhost:8083/connectors/ -d '{"name": "sde-connector", "config": {"connector.class": "io.debezium.connector.postgresql.PostgresConnector", "database.hostname": "postgres", "database.port": "5432", "database.user": "start_data_engineer", "database.password": "password", "database.dbname" : "start_data_engineer", "database.server.name": "bankserver1", "table.whitelist": "bank.holding"}}'

```
* Let’s check for presence of connector: `curl -H "Accept:application/json" localhost:8083/connectors/`
* We can see the sde-connector is registered.
* Now we can start our python script database_test_writes.py to populate amoun of data. Script inserts every 3 seconds to table a new data.
* Run this command in Terminal: 
```
python3 database_test_writes.py

```
* After this we can visit MiniO console, [localhost:9000/](http://localhost:9001/buckets) login:minioadmin; password:minioadmin;
* We can check, that our python service wraps every 10 messages from kafka topic to one json file and saves it in MiniO bucket.



