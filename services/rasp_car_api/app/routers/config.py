# Implementation of route to send API
# main/routers/pressure.py
from fastapi import APIRouter, Depends, HTTPException
from app import schemas

router = APIRouter()

# Edit Dict to modify configs

@router.get("/config/", response_model=list[schemas.Distance])
def read_distances(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_distances(db=db, skip=skip, limit=limit)
