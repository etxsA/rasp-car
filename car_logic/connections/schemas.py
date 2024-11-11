# Definition of Schemas
# For serialization and validationS
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# 1. Photoresistor Schemas
class PhotoresistorBase(BaseModel):
    voltage: float
    lightLevel: float
    timestamp: Optional[datetime] = None #If not provided, it will be generated

class PhotoresistorCreate(PhotoresistorBase):
    pass

# 2. Accelerometer Schemas
class AccelerometerBase(BaseModel):
    x: float
    y: float
    z: float
    events: str
    timestamp: Optional[datetime] = None

class AccelerometerCreate(AccelerometerBase):
    pass

# 3. Distance Schemas
class DistanceBase(BaseModel):
    distance: float
    timestamp: Optional[datetime] = None

class DistanceCreate(DistanceBase):
    pass

# 4. Pressure Schemas
class PressureBase(BaseModel):
    temperature: float
    pressure: float
    altitude: float
    timestamp: Optional[datetime] = None

class PressureCreate(PressureBase):
    pass
