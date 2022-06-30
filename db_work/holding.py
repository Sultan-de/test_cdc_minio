from sqlalchemy import Column, String, Integer, Date

from base import Base


class Holding(Base):
    __tablename__ = 'holding'

    holding_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    holding_stock = Column(String(8))
    holding_quantity = Column(Integer)
    datetime_created = Column(Date)
    datetime_updated = Column(Date)

    def __init__(self, holding_id, user_id, holding_stock, holding_quantity, datetime_created, datetime_updated):
        self.holding_id = holding_id
        self.user_id = user_id
        self.holding_stock = holding_stock
        self.holding_quantity = holding_quantity
        self.datetime_created = datetime_created
        self.datetime_updated = datetime_updated
