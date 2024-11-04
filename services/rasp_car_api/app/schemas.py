# Definition of Schemas
# For serialization and validation
# main/schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# 1. Photoresistor Schemas
class PhotoresistorBase(BaseModel):
    analog_voltage: int
    voltage: float
    timestamp: Optional[datetime] = None #If not provided, it will be generated

class PhotoresistorCreate(PhotoresistorBase):
    pass

# Set ORM MODE it will be used for every single class
class Photoresistor(PhotoresistorBase):
    id: int

    class Config:
        orm_mode = True

# 2. Accelerometer Schemas
class AccelerometerBase(BaseModel):
    x_axis: float
    y_axis: float
    z_axis: float
    free_fall: bool
    timestamp: Optional[datetime] = None

class AccelerometerCreate(AccelerometerBase):
    pass

class Accelerometer(AccelerometerBase):
    id: int

    class Config:
        orm_mode = True

# 3. Distance Schemas
class DistanceBase(BaseModel):
    distance: float
    timestamp: Optional[datetime] = None

class DistanceCreate(DistanceBase):
    pass

class Distance(DistanceBase):
    id: int

    class Config:
        orm_mode = True

# 4. Pressure Schemas
class PressureBase(BaseModel):
    temperature: float
    pressure: float
    altitude: float
    timestamp: Optional[datetime] = None

class PressureCreate(PressureBase):
    pass

class Pressure(PressureBase):
    id: int

    class Config:
        orm_mode = True
