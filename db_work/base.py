from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://start_data_engineer:password@localhost:5432/start_data_engineer')
Session = sessionmaker(bind=engine)

Base = declarative_base()
