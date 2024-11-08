# Implementation of routes used for the distance table. 
# main/routers/pressure.py
from fastapi import APIRouter, Depends, HTTPException
from app import crud, schemas
from app.database import get_db

router = APIRouter()


@router.get("/config/", response_model=list[schemas.Distance])
def read_distances(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_distances(db=db, skip=skip, limit=limit)