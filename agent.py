from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Agent(Base):
    __tablename__ = 'agents'
    agent_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    address_line_1 = Column(String(90))
    address_line_2 = Column(String(50), nullable=True)
    city = Column(String(30))
    state = Column(String(2))
    zip = Column(String(5))
    phone = Column(String(15))
    start_date = Column(Date)
    created_at = Column(DateTime)