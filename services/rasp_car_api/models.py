# Definition of ORM models for SQLAlchemy
# main/models.py
from sqlalchemy import Column, Integer, String
from .database import Base

class Sensor1(Base):
    __tablename__ = "s1"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

