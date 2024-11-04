# Implementation of routes used for the pressure table. 
# main/routers/pressure.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/pressure/", response_model=schemas.Pressure)
def create_pressure(
    pressure: schemas.PressureCreate, db: Session = Depends(get_db)
):
    return crud.create_pressure(db=db, pressure=pressure)

@router.get("/pressure/{pressure_id}", response_model=schemas.Pressure)
def read_pressure(pressure_id: int, db: Session = Depends(get_db)):
    db_pressure = crud.get_pressure(db, pressure_id=pressure_id)
    if db_pressure is None:
        raise HTTPException(status_code=404, detail="Pressure record not found")
    return db_pressure

@router.get("/pressure/", response_model=list[schemas.Pressure])
def read_pressures(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_pressures(db=db, skip=skip, limit=limit)

@router.delete("/pressure/{pressure_id}", response_model=schemas.Pressure)
def delete_pressure(pressure_id: int, db: Session = Depends(get_db)):
    db_pressure = crud.delete_pressure(db=db, pressure_id=pressure_id)
    if db_pressure is None:
        raise HTTPException(status_code=404, detail="Pressure record not found")
    return db_pressure
