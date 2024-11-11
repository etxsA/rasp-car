# Database Connection and Setup with SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from . import models
from .models import get_utc_now
from . import schemas




class DBController:

    def __init__(self, URL: str) -> None:
        self.engine = create_engine(URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
    

    def _get_db(self) -> object:
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
    

    def send_photoresistor(self, photoresistor: schemas.PhotoresistorCreate):
        db = self._get_db()
        db_photoresistor = models.Photoresistor(
            voltage=photoresistor.voltage,
            lightLevel=photoresistor.lightLevel,
            timestamp=photoresistor.timestamp or get_utc_now()
        )
        db.add(db_photoresistor)
        db.commit()
        db.refresh(db_photoresistor)
        return db_photoresistor

    ## Accelerometer operations
    def send_accelerometer(self, accelerometer: schemas.AccelerometerCreate):
        db = self._get_db()
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


    ## Distance Operations
    def send_distance(self, distance: schemas.DistanceCreate):
        db = self._get_db()
        db_distance = models.Distance(
            distance=distance.distance,
            timestamp=distance.timestamp or get_utc_now()
        )
        db.add(db_distance)
        db.commit()
        db.refresh(db_distance)
        return db_distance

    # Pressure Operations
    def send_pressure(self, pressure: schemas.PressureCreate):
        db = self._get_db()
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
