# Implementation of routes used for the distance table. 
# main/routers/pressure.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/distance/", response_model=schemas.Distance)
def create_distance(
    distance: schemas.DistanceCreate, db: Session = Depends(get_db)
):
    return crud.create_distance(db=db, distance=distance)

@router.get("/distance/{distance_id}", response_model=schemas.Distance)
def read_distance(distance_id: int, db: Session = Depends(get_db)):
    db_distance = crud.get_distance(db, distance_id=distance_id)
    if db_distance is None:
        raise HTTPException(status_code=404, detail="Distance record not found")
    return db_distance

@router.get("/distance/", response_model=list[schemas.Distance])
def read_distances(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_distances(db=db, skip=skip, limit=limit)

@router.delete("/distance/{distance_id}", response_model=schemas.Distance)
def delete_distance(distance_id: int, db: Session = Depends(get_db)):
    db_distance = crud.delete_distance(db=db, distance_id=distance_id)
    if db_distance is None:
        raise HTTPException(status_code=404, detail="Distance record not found")
    return db_distance
