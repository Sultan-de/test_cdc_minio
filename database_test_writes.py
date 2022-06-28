import psycopg2
import datetime
import time 

sql_insert = """INSERT INTO bank.holding
         VALUES(%s, %s, %s, %s, %s, %s)"""
 
conn = None
holding_id = 1000
dict_data = {
	'id': 2, 
	'data': 'SP500', 
	'h_id': 1, 
	'create_time': datetime.datetime.now(), 
	'update_time': datetime.datetime.now(),
}
while True:
	# print(sql_insert.format(holding_id,dict_data['id'], dict_data['data'], dict_data['h_id'], dict_data['create_time'], dict_data['update_time']))
	holding_id += 1
	try:
		conn = psycopg2.connect(
			host="localhost",
			database="start_data_engineer",
			user="start_data_engineer",
			password="password"
		)
		cur = conn.cursor()
		cur.execute(sql_insert, (holding_id, dict_data['id'], dict_data['data'], dict_data['h_id'], dict_data['create_time'], dict_data['update_time']))
		conn.commit()
		time.sleep(3)
		print("Data inserted:", holding_id)

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()