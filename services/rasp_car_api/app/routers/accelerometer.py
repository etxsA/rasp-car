# Implementation of routes used for the accelerometer table. 
# main/routers/acceleromter.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from datetime import datetime

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
def read_photoresistors(
    skip: int = 0,
    limit: int = 10,
    min_x: float = Query(None, description="Minimum x to filter results"),
    min_y: float = Query(None, description="Minimum y to filter results"),
    min_z: float = Query(None, description="Minimum z to filter results"),
    start_date: str = Query(None, description="Start date to filter results (format: YYYY-MM-DDTHH:MM:SS)"),
    end_date: str = Query(None, description="End date to filter results (format: YYYY-MM-DDTHH:MM:SS)"),
    db: Session = Depends(get_db)
):
    # Convert start_date and end_date to datetime objects if provided
    start_datetime = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S") if start_date else None
    end_datetime = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S") if end_date else None

    return crud.get_accelerometers(
        db=db,
        skip=skip,
        limit=limit,
        start_date=start_datetime,
        end_date=end_datetime,
        min_x=min_x,
        min_y=min_y,
        min_z=min_z
    )

@router.delete("/accelerometer/{accelerometer_id}", response_model=schemas.Accelerometer)
def delete_accelerometer(accelerometer_id: int, db: Session = Depends(get_db)):
    db_accelerometer = crud.delete_accelerometer(db=db, accelerometer_id=accelerometer_id)
    if db_accelerometer is None:
        raise HTTPException(status_code=404, detail="Accelerometer not found")
    return db_accelerometer
