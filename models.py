from sqlalchemy import Column, Integer, String
from database import Base

# Define To Do class inheriting from Base
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    key = Column(String(256))
    balance = Column(Integer)
    logs = Column(String(256))
