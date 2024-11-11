# Main app
# main.py

from fastapi import FastAPI
from app import models
from app.routers import photoresistor, accelerometer, distance, pressure, config
from app.database import engine

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(photoresistor.router)
app.include_router(accelerometer.router)
app.include_router(distance.router)
app.include_router(pressure.router)

# Configuration endpoint 
app.include_router(config.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastApi for rasp-car project!"}
