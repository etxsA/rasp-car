# Implementation of routes used for the distance table. 
# main/routers/pressure.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from datetime import datetime

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
def read_distances(
    skip: int = 0,
    limit: int = 10,
    min_distance: float = Query(None, description="Minimum distance to filter results"),
    start_date: str = Query(None, description="Start date to filter results (format: YYYY-MM-DDTHH:MM:SS)"),
    end_date: str = Query(None, description="End date to filter results (format: YYYY-MM-DDTHH:MM:SS)"),
    db: Session = Depends(get_db)
):
    # Convert start_date and end_date to datetime objects if provided
    start_datetime = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S") if start_date else None
    end_datetime = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S") if end_date else None

    return crud.get_distances(
        db=db,
        skip=skip,
        limit=limit,
        min_distance=min_distance,
        start_date=start_datetime,
        end_date=end_datetime
    )

@router.delete("/distance/{distance_id}", response_model=schemas.Distance)
def delete_distance(distance_id: int, db: Session = Depends(get_db)):
    db_distance = crud.delete_distance(db=db, distance_id=distance_id)
    if db_distance is None:
        raise HTTPException(status_code=404, detail="Distance record not found")
    return db_distance
