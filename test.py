
from kafka import KafkaConsumer
import json
import io
from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv
import os


#load_dotenv()

def write_to_minio(file_bytes, file_buffer, file_name):
# Create a client with the MinIO server playground, its access key
# and secret key.
	client = Minio(
		endpoint = "minio1:9000",
		access_key="minioadmin",	#os.environ.get('MINIO_ROOT_USER'),
		secret_key="minioadmin",		#os.environ.get('MINIO_ROOT_PASSWORD'),
		# region='kz',
		secure=False,
	)

	# Make 'asiatrip' bucket if not exist.
	found = client.bucket_exists("asiatrip")
	if not found:
		client.make_bucket("asiatrip")
	else:
		print("Bucket 'asiatrip' already exists")
	
	client.put_object(
		"asiatrip", file_name, data = file_buffer, length = len(file_bytes), content_type='application/json'
	)
	print(
		f"{file_name} - is successfully uploaded as "
		f"object '{file_name}' to bucket 'asiatrip'."
	)


COUNT_OF_MSGS = 1
consumer = KafkaConsumer(
	'bankserver1.bank.holding',
	bootstrap_servers=['kafka:9092'],
	auto_offset_reset='earliest',
	enable_auto_commit=True,
	value_deserializer=lambda x: json.loads(x.decode('utf-8')))		
level_num = 0
list_of_messages = []
for message in consumer:
	if COUNT_OF_MSGS == 10:
		COUNT_OF_MSGS = 1
		message = message.value
		list_of_messages.append(str(message))
		to_file = ';'.join(list_of_messages)
		file_bytes = str.encode(to_file)
		file_buffer = io.BytesIO(file_bytes)

		print(file_buffer)
		print(list_of_messages)

		write_to_minio(file_bytes,file_buffer, f'data_chunk_{COUNT_OF_MSGS}_{level_num}.json')
		
		list_of_messages.clear()
		level_num += 1
	else:
		message = message.value
		list_of_messages.append(str(message))
		COUNT_OF_MSGS += 1

