# Main app
# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware
from app import models
from app.routers import photoresistor, accelerometer, distance, pressure, config
from app.database import engine
from app.mqtt import lifespan

# Add lifespan to run mqtt server
app = FastAPI(lifespan=lifespan)

# CORS configuration
origins = [
    "http://127.0.0.1:3000",  # Replace with the frontend's URL
    "http://localhost:3000"    # Include localhost if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
