# Implementation of routes used for the photoresistor table. 
# main/routers/photoresistor.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .. import crud, schemas
from datetime import datetime
from ..database import get_db

router = APIRouter()

@router.post("/photoresistor/", response_model=schemas.Photoresistor)
def create_photoresistor(
    photoresistor: schemas.PhotoresistorCreate, db: Session = Depends(get_db)
):
    return crud.create_photoresistor(db=db, photoresistor=photoresistor)

@router.get("/photoresistor/{photoresistor_id}", response_model=schemas.Photoresistor)
def read_photoresistor(photoresistor_id: int, db: Session = Depends(get_db)):
    db_photoresistor = crud.get_photoresistor(db, photoresistor_id=photoresistor_id)
    if db_photoresistor is None:
        raise HTTPException(status_code=404, detail="Photoresistor entry not found")
    return db_photoresistor

@router.get("/photoresistor/", response_model=list[schemas.Photoresistor])
def read_photoresistors(
    skip: int = 0,
    limit: int = 10,
    min_voltage: float = Query(None, description="Minimum voltage to filter results"),
    start_date: str = Query(None, description="Start date to filter results (format: YYYY-MM-DDTHH:MM:SS)"),
    end_date: str = Query(None, description="End date to filter results (format: YYYY-MM-DDTHH:MM:SS)"),
    db: Session = Depends(get_db)
):
    # Convert start_date and end_date to datetime objects if provided
    start_datetime = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S") if start_date else None
    end_datetime = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S") if end_date else None
    
    return crud.get_photoresistors(
        db=db,
        skip=skip,
        limit=limit,
        min_voltage=min_voltage,
        start_date=start_datetime,
        end_date=end_datetime
    )


@router.delete("/photoresistor/{photoresistor_id}", response_model=schemas.Photoresistor)
def delete_photoresistor(photoresistor_id: int, db: Session = Depends(get_db)):
    db_photoresistor = crud.delete_photoresistor(db=db, photoresistor_id=photoresistor_id)
    if db_photoresistor is None:
        raise HTTPException(status_code=404, detail="Photoresistor not found")
    return db_photoresistor
