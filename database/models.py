from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, nullable=False, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)