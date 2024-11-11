# Definition of ORM models for SQLAlchemy
from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

def get_utc_now():
    return datetime.now(timezone.utc)

Base = declarative_base()

class Photoresistor(Base):
    __tablename__ = "photoresistor"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    voltage = Column(Float, nullable=False)
    lightLevel = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=get_utc_now)

class Accelerometer(Base):
    __tablename__ = "accelerometer"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    z = Column(Float, nullable=False)
    events = Column(String(20), nullable=False)
    timestamp = Column(DateTime, default=get_utc_now)

class Distance(Base):
    __tablename__ = "distance"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    distance = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=get_utc_now)

class Pressure(Base):
    __tablename__ = "pressure"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    temperature = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)
    altitude = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=get_utc_now)
