# Definition of the controllers for the CRUD functionality of the api
# main/crud.py
from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime
from app.models import get_utc_now

# 1. Photoresistor CRUD operations

def create_photoresistor(db: Session, photoresistor: schemas.PhotoresistorCreate):
    db_photoresistor = models.Photoresistor(
        voltage=photoresistor.voltage,
        lightLevel=photoresistor.lightLevel,
        timestamp=photoresistor.timestamp or get_utc_now()
    )
    db.add(db_photoresistor)
    db.commit()
    db.refresh(db_photoresistor)
    return db_photoresistor

def get_photoresistor(db: Session, photoresistor_id: int):
    return db.query(models.Photoresistor).filter(models.Photoresistor.id == photoresistor_id).first()

def get_photoresistors(db: Session, skip: int = 0, limit: int = 10, min_voltage: float = None, start_date: str = None, end_date: str = None):
    print(f"Filtering with min_voltage: {min_voltage}, start_date: {start_date}, end_date: {end_date}")
    
    # Start building the query
    query = db.query(models.Photoresistor)

    if min_voltage is not None:
        query = query.filter(models.Photoresistor.voltage >= min_voltage)
    
    if start_date:
        query = query.filter(models.Photoresistor.timestamp >= start_date)
    
    if end_date:
        query = query.filter(models.Photoresistor.timestamp <= end_date)
    
    return query.offset(skip).limit(limit).all()


def delete_photoresistor(db: Session, photoresistor_id: int):
    db_photoresistor = get_photoresistor(db, photoresistor_id)
    if db_photoresistor:
        db.delete(db_photoresistor)
        db.commit()
    return db_photoresistor

## Accelerometer operations
def create_accelerometer(db: Session, accelerometer: schemas.AccelerometerCreate):
    db_accelerometer = models.Accelerometer(
        x=accelerometer.x,
        y=accelerometer.y,
        z=accelerometer.z,
        events=accelerometer.events,
        timestamp=accelerometer.timestamp or get_utc_now()
    )
    db.add(db_accelerometer)
    db.commit()
    db.refresh(db_accelerometer)
    return db_accelerometer

def get_accelerometer(db: Session, accelerometer_id: int):
    return db.query(models.Accelerometer).filter(models.Accelerometer.id == accelerometer_id).first()

def get_accelerometers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Accelerometer).offset(skip).limit(limit).all()

def delete_accelerometer(db: Session, accelerometer_id: int):
    db_accelerometer = get_accelerometer(db, accelerometer_id)
    if db_accelerometer:
        db.delete(db_accelerometer)
        db.commit()
    return db_accelerometer

## Distance Operations
def create_distance(db: Session, distance: schemas.DistanceCreate):
    db_distance = models.Distance(
        distance=distance.distance,
        timestamp=distance.timestamp or get_utc_now()
    )
    db.add(db_distance)
    db.commit()
    db.refresh(db_distance)
    return db_distance

def get_distance(db: Session, distance_id: int):
    return db.query(models.Distance).filter(models.Distance.id == distance_id).first()

def get_distances(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Distance).offset(skip).limit(limit).all()

def delete_distance(db: Session, distance_id: int):
    db_distance = get_distance(db, distance_id)
    if db_distance:
        db.delete(db_distance)
        db.commit()
    return db_distance

# Pressure Operations
def create_pressure(db: Session, pressure: schemas.PressureCreate):
    db_pressure = models.Pressure(
        temperature=pressure.temperature,
        pressure=pressure.pressure,
        altitude=pressure.altitude,
        timestamp=pressure.timestamp or get_utc_now()
    )
    db.add(db_pressure)
    db.commit()
    db.refresh(db_pressure)
    return db_pressure

def get_pressure(db: Session, pressure_id: int):
    return db.query(models.Pressure).filter(models.Pressure.id == pressure_id).first()

def get_pressures(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Pressure).offset(skip).limit(limit).all()

def delete_pressure(db: Session, pressure_id: int):
    db_pressure = get_pressure(db, pressure_id)
    if db_pressure:
        db.delete(db_pressure)
        db.commit()
    return db_pressure
