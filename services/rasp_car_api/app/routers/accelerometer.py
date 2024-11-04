# Implementation of routes used for the accelerometer table. 
# main/routers/acceleromter.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/accelerometer/", response_model=schemas.Accelerometer)
def create_accelerometer(
    accelerometer: schemas.AccelerometerCreate, db: Session = Depends(get_db)
):
    return crud.create_accelerometer(db=db, accelerometer=accelerometer)

@router.get("/accelerometer/{accelerometer_id}", response_model=schemas.Accelerometer)
def read_accelerometer(accelerometer_id: int, db: Session = Depends(get_db)):
    db_accelerometer = crud.get_accelerometer(db, accelerometer_id=accelerometer_id)
    if db_accelerometer is None:
        raise HTTPException(status_code=404, detail="Accelerometer not found")
    return db_accelerometer

@router.get("/accelerometer/", response_model=list[schemas.Accelerometer])
def read_accelerometers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_accelerometers(db=db, skip=skip, limit=limit)

@router.delete("/accelerometer/{accelerometer_id}", response_model=schemas.Accelerometer)
def delete_accelerometer(accelerometer_id: int, db: Session = Depends(get_db)):
    db_accelerometer = crud.delete_accelerometer(db=db, accelerometer_id=accelerometer_id)
    if db_accelerometer is None:
        raise HTTPException(status_code=404, detail="Accelerometer not found")
    return db_accelerometer
