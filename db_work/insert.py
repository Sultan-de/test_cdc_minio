import datetime
import time

from base import Session, engine, Base
from holding import Holding

Base.metadata.create_all(engine)

session = Session()

holding_id = 1000

connection = engine.connect()
query = f'ALTER TABLE holding replica identity FULL; ;'
connection.execute(query)

while True:
    holding_id += 1
    user_id = 2
    holding_stock = 'SP500'
    holding_quantity = 1
    datetime_created = datetime.datetime.now()
    datetime_updated = datetime.datetime.now()

    new_object = Holding(
        holding_id=holding_id,
        user_id=user_id,
        holding_stock=holding_stock,
        holding_quantity=holding_quantity,
        datetime_created=datetime_created,
        datetime_updated=datetime_updated,
    )

    session.add(new_object)
    session.commit()
    print(f'Object - {holding_id} inserted')
    time.sleep(10)

session.close()
