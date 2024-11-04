# Definition of the controllers for the CRUD functionality of the api
# main/crud.py
from sqlalchemy.orm import Session
from app import models, schemas
from app.models import get_utc_now


# 1. Photoresistor CRUD operations
def create_photoresistor(db: Session, photoresistor: schemas.PhotoresistorCreate):
    db_photoresistor = models.Photoresistor(
        analog_voltage=photoresistor.analog_voltage,
        voltage=photoresistor.voltage,
        timestamp=photoresistor.timestamp or get_utc_now()
    )
    db.add(db_photoresistor)
    db.commit()
    db.refresh(db_photoresistor)
    return db_photoresistor

def get_photoresistor(db: Session, photoresistor_id: int):
    return db.query(models.Photoresistor).filter(models.Photoresistor.id == photoresistor_id).first()

def get_photoresistors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Photoresistor).offset(skip).limit(limit).all()

def delete_photoresistor(db: Session, photoresistor_id: int):
    db_photoresistor = get_photoresistor(db, photoresistor_id)
    if db_photoresistor:
        db.delete(db_photoresistor)
        db.commit()
    return db_photoresistor

# 2. Accelerometer CRUD operations
def create_accelerometer(db: Session, accelerometer: schemas.AccelerometerCreate):
    db_accelerometer = models.Accelerometer(
        x_axis=accelerometer.x_axis,
        y_axis=accelerometer.y_axis,
        z_axis=accelerometer.z_axis,
        free_fall=accelerometer.free_fall,
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

# 3. Distance CRUD operations
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

# 4. Pressure CRUD operations
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
